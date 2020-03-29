import ptvsd
import pandas as pd
from datetime import datetime, timedelta
import numpy

# Configuração do debbuger
ptvsd.enable_attach(address=('0.0.0.0', 5678), redirect_output=True)
ptvsd.wait_for_attach()


class CSVInvalido(Exception):
    """"CSV Invalido"""
    pass


class PeriodoInvalido(Exception):
    """Periodo Invalido"""
    pass


class FundoInvestimento():
    """Classe global que avalia series de dados formatados relacionados a fundos de investimento"""

    def __init__(self, serie_dados_fundo_path, serie_dados_cdi_path):
        self.serie_dados_fundo = self._valida_serie_investimento(
            serie_dados_fundo_path)
        self.serie_dados_cdi = self._valida_serie_cdi(serie_dados_cdi_path)

    def _valida_serie_investimento(self, serie_dados_fundo_path):
        """Metodo interno que valida o formato da serie de investimentos e retorna caso valido"""
        try:
            df_serie_fundo = pd.read_csv(serie_dados_fundo_path, decimal=',')
            if df_serie_fundo.empty:
                raise CSVInvalido("Nao ha dados no CSV")
            return df_serie_fundo
        except:
            raise CSVInvalido("CSV Invalido")

    def _valida_serie_cdi(self, serie_dados_cdi_path):
        """Metodo que valida o formato da serie de CDI e retorna caso valido"""
        try:
            df_serie_cdi = pd.read_csv(serie_dados_cdi_path, decimal=',')
            if df_serie_cdi.empty:
                raise CSVInvalido("Nao ha dados no CSV")
            return df_serie_cdi
        except:
            raise CSVInvalido("CSV Invalido")

    def _formatador_simples(self, valor, unidade='%'):
        if unidade == 'R$':
            return 'R$ {:.2f}'.format(valor * 100).replace('.', ',')
        return '{:.4f} %'.format(valor * 100).replace('.', ',')

    def rentabilidade_periodo(self, data_inicio_str, data_fim_str):
        valor_cota_final = self.serie_dados_fundo.loc[self.serie_dados_fundo['data'] == data_fim_str]
        valor_cota_inicial = self.serie_dados_fundo.loc[self.serie_dados_fundo['data']
                                                        == data_inicio_str]

        if valor_cota_final.empty or valor_cota_inicial.empty:
            raise PeriodoInvalido('Periodo invalido')

        valor_cota_anterior_inicial = self.serie_dados_fundo.iloc[valor_cota_inicial.index - 1]
        rentabilidade_periodo = float(
            valor_cota_final.iat[0, 1])/float(valor_cota_anterior_inicial.iat[0, 1]) - 1
        return {'descricao': 'rentabilidade_periodo', 'valor': rentabilidade_periodo, 'valor_formatado': self._formatador_simples(rentabilidade_periodo)}

    def rentabilidade_relativa_cdi(self, data_inicio_str, data_fim_str):
        mask_query = (self.serie_dados_cdi['date'] >= data_inicio_str) & (
            self.serie_dados_cdi['date'] <= data_fim_str)
        aux_intervalo_cdi = self.serie_dados_cdi.loc[mask_query]
        aux_intervalo_cdi_numeric = pd.to_numeric(
            aux_intervalo_cdi['variacao_diaria'].str.replace('%', ''))
        aux_intervalo_cdi_numeric /= 100
        aux_intervalo_cdi_numeric += 1
        cdi_intervalo = (numpy.prod(
            aux_intervalo_cdi_numeric.tolist()) - 1)/10000
        rentabilidade_periodo = self.rentabilidade_periodo(
            '2019-01-02', '2019-01-31')['valor']
        rentabilidade_relativa_cdi = (
            rentabilidade_periodo / cdi_intervalo-1)/10000
        return {'descricao': 'rentabilidade_relativa_cdi', 'valor': rentabilidade_relativa_cdi,
                'valor_formatado': self._formatador_simples(rentabilidade_relativa_cdi)}

    def evolucao_patrimonio(self, data_inicio_str, data_fim_str):
        valor_patrimonio_final = self.serie_dados_fundo.loc[
            self.serie_dados_fundo['data'] == data_fim_str]
        valor_patrimonio_inicial = self.serie_dados_fundo.loc[self.serie_dados_fundo['data']
                                                              == data_inicio_str]

        if valor_patrimonio_final.empty or valor_patrimonio_inicial.empty:
            raise PeriodoInvalido('Periodo invalido')

        valor_patrimonio_anterior_inicial = self.serie_dados_fundo.iloc[
            valor_patrimonio_inicial.index - 1]
        evolucao_patrimonio = float(
            valor_patrimonio_final.iat[0, 2])-float(valor_patrimonio_anterior_inicial.iat[0, 2])
        return {'descricao': 'evolucao_patrimonio', 'valor': evolucao_patrimonio, 'valor_formatado': self._formatador_simples(evolucao_patrimonio, unidade='R$')}

    def _retorno_diario(self, data_inicio_str, data_fim_str):
        valor_cota_final = self.serie_dados_fundo.loc[self.serie_dados_fundo['data'] == data_fim_str]
        valor_cota_inicial = self.serie_dados_fundo.loc[self.serie_dados_fundo['data']
                                                        == data_inicio_str]

        if valor_cota_final.empty or valor_cota_inicial.empty:
            raise PeriodoInvalido('Periodo invalido')

        aux_intervalo_cota = self.serie_dados_fundo.iloc[valor_cota_inicial.index.values.max(
        ) - 1:valor_cota_final.index.values.max()]
        aux_intervalo_cota_numeric_dict = pd.to_numeric(
            aux_intervalo_cota['cota']).to_dict()
        list_variacao_retorno = []
        for index, (key, value) in enumerate(aux_intervalo_cota_numeric_dict.items()):
            if index > 0:
                list_variacao_retorno.append({'data': self.serie_dados_fundo.iloc[key]['data'],
                                              'valor': value / list(aux_intervalo_cota_numeric_dict.values())[index - 1] - 1,
                                              'valor_formatado': self._formatador_simples(value / list(aux_intervalo_cota_numeric_dict.values())[index - 1] - 1)})

        return list_variacao_retorno

    def maior_retorno_diario(self, data_inicio_str, data_fim_str):
        maior_retorno_diario = {'descricao': 'maior_retorno_diario'}
        maior_retorno_diario.update(sorted(self._retorno_diario(
            data_inicio_str, data_fim_str), key=lambda k: k['valor'])[-1])
        return maior_retorno_diario

    def menor_retorno_diario(self, data_inicio_str, data_fim_str):
        menor_retorno_diario = {'descricao': 'menor_retorno_diario'}
        menor_retorno_diario.update(sorted(self._retorno_diario(
            data_inicio_str, data_fim_str), key=lambda k: k['valor'])[0])
        return menor_retorno_diario


"""Cria uma nova instancia do fundo Zarathustra"""
fundo_zarathustra = FundoInvestimento(
    'data_files/zarathustra.csv', 'data_files/cdi.csv')

"""Executa os metodos classe FundoInvestimento"""
print(fundo_zarathustra.rentabilidade_periodo('2019-01-02', '2019-01-31'))
print(fundo_zarathustra.rentabilidade_relativa_cdi('2019-01-02', '2019-01-31'))
print(fundo_zarathustra.evolucao_patrimonio('2019-01-02', '2019-01-31'))
print(fundo_zarathustra.maior_retorno_diario('2019-01-02', '2019-01-31'))
print(fundo_zarathustra.menor_retorno_diario('2019-01-02', '2019-01-31'))

import unittest
from main import FundoInvestimento


class TestFundoInvestimento(unittest.TestCase):

    def test_rentabilidade_periodo(self):
        result = {'descricao': 'rentabilidade_periodo',
                  'valor': 0.02540562914725064, 'valor_formatado': '2,5406 %'}
        fundo_zarathustra = FundoInvestimento(
            'data_files/zarathustra.csv', 'data_files/cdi.csv')
        self.assertEqual(fundo_zarathustra.rentabilidade_periodo(
            '2019-01-02', '2019-01-31'), result)

    def test_rentabilidade_relativa_cdi(self):
        result = {'descricao': 'rentabilidade_relativa_cdi',
                  'valor': 4.678668003492553, 'valor_formatado': '467,8668 %'}
        fundo_zarathustra = FundoInvestimento(
            'data_files/zarathustra.csv', 'data_files/cdi.csv')
        self.assertEqual(fundo_zarathustra.rentabilidade_relativa_cdi(
            '2019-01-02', '2019-01-31'), result)

    def test_evolucao_patrimonio(self):
        result = {'descricao': 'evolucao_patrimonio',
                  'valor': 52828272.10000001, 'valor_formatado': 'R$ 5282827210,00'}
        fundo_zarathustra = FundoInvestimento(
            'data_files/zarathustra.csv', 'data_files/cdi.csv')
        self.assertEqual(fundo_zarathustra.evolucao_patrimonio(
            '2019-01-02', '2019-01-31'), result)

    def test_maior_retorno_diario(self):
        result = {'descricao': 'maior_retorno_diario', 'data': '2019-01-02',
                  'valor': 0.013983120538590743, 'valor_formatado': '1,3983 %'}
        fundo_zarathustra = FundoInvestimento(
            'data_files/zarathustra.csv', 'data_files/cdi.csv')
        self.assertEqual(fundo_zarathustra.maior_retorno_diario(
            '2019-01-02', '2019-01-31'), result)

    def test_menor_retorno_diario(self):
        result = {'descricao': 'menor_retorno_diario', 'data': '2019-01-07',
                  'valor': -0.009555771613943387, 'valor_formatado': '-0,9556 %'}
        fundo_zarathustra = FundoInvestimento(
            'data_files/zarathustra.csv', 'data_files/cdi.csv')
        self.assertEqual(fundo_zarathustra.menor_retorno_diario(
            '2019-01-02', '2019-01-31'), result)

    def test_serie_retorno_acumado(self):
        result = {'descricao': 'serie_retorno_acumado', 'serie': [{'data': '2019-01-02', 'valor': 0.013983120538590743, 'valor_formatado': '1,3983 %'}, {'data': '2019-01-03', 'valor': 0.015574717919099701, 'valor_formatado': '1,5575 %'}, {'data': '2019-01-04', 'valor': 0.013133347262685668, 'valor_formatado': '1,3133 %'}, {'data': '2019-01-07', 'valor': 0.0035775756487422816, 'valor_formatado': '0,3578 %'}, {'data': '2019-01-08', 'valor': 0.004801416763407063, 'valor_formatado': '0,4801 %'}, {'data': '2019-01-09', 'valor': 0.007984458506736236, 'valor_formatado': '0,7984 %'}, {'data': '2019-01-10', 'valor': 0.004187036470112759, 'valor_formatado': '0,4187 %'}, {'data': '2019-01-11', 'valor': 0.003969013247787534, 'valor_formatado': '0,3969 %'}, {'data': '2019-01-14', 'valor': 0.009080465708840024, 'valor_formatado': '0,9080 %'}, {'data': '2019-01-15', 'valor': 0.004959378629701416, 'valor_formatado': '0,4959 %'}, {'data': '2019-01-16', 'valor': 0.004196773598292847, 'valor_formatado': '0,4197 %'}, {
            'data': '2019-01-17', 'valor': 0.007217981121943717, 'valor_formatado': '0,7218 %'}, {'data': '2019-01-18', 'valor': 0.006128797923945384, 'valor_formatado': '0,6129 %'}, {'data': '2019-01-21', 'valor': 0.005304685761905126, 'valor_formatado': '0,5305 %'}, {'data': '2019-01-22', 'valor': 0.005217343220993209, 'valor_formatado': '0,5217 %'}, {'data': '2019-01-23', 'valor': 0.0101853604396549, 'valor_formatado': '1,0185 %'}, {'data': '2019-01-24', 'valor': 0.012900492120209606, 'valor_formatado': '1,2900 %'}, {'data': '2019-01-25', 'valor': 0.012411581835746754, 'valor_formatado': '1,2412 %'}, {'data': '2019-01-28', 'valor': 0.009157110932431545, 'valor_formatado': '0,9157 %'}, {'data': '2019-01-29', 'valor': 0.013287302398875989, 'valor_formatado': '1,3287 %'}, {'data': '2019-01-30', 'valor': 0.014010557780038457, 'valor_formatado': '1,4011 %'}, {'data': '2019-01-31', 'valor': 0.02536991057653748, 'valor_formatado': '2,5370 %'}]}
        fundo_zarathustra = FundoInvestimento(
            'data_files/zarathustra.csv', 'data_files/cdi.csv')
        self.assertEqual(fundo_zarathustra.serie_retorno_acumado(
            '2019-01-02', '2019-01-31'), result)
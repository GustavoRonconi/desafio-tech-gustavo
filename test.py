import unittest
from main import FundoInvestimento


class TestFundoInvestimento(unittest.TestCase):

    def test_rentabilidade_periodo(self):
        result = {'descricao': 'rentabilidade_periodo', 'valor': 0.02540562914725064, 'valor_formatado': '2,5406 %'}
        fundo_zarathustra = FundoInvestimento('data_files/zarathustra.csv', 'data_files/cdi.csv')
        self.assertEqual(fundo_zarathustra.rentabilidade_periodo('2019-01-02', '2019-01-31'), result)
    
    def test_rentabilidade_relativa_cdi(self):
        result = {'descricao': 'rentabilidade_relativa_cdi', 'valor': 4.678668003492553, 'valor_formatado': '467,8668 %'}
        fundo_zarathustra = FundoInvestimento('data_files/zarathustra.csv', 'data_files/cdi.csv')
        self.assertEqual(fundo_zarathustra.rentabilidade_relativa_cdi('2019-01-02', '2019-01-31'), result)
    
    def test_evolucao_patrimonio(self):
        result = {'descricao': 'evolucao_patrimonio', 'valor': 52828272.10000001, 'valor_formatado': 'R$ 5282827210,00'}
        fundo_zarathustra = FundoInvestimento('data_files/zarathustra.csv', 'data_files/cdi.csv')
        self.assertEqual(fundo_zarathustra.evolucao_patrimonio('2019-01-02', '2019-01-31'), result)
    
    def test_maior_retorno_diario(self):
        result = {'descricao': 'maior_retorno_diario', 'data': '2019-01-02', 'valor': 0.013983120538590743, 'valor_formatado': '1,3983 %'}
        fundo_zarathustra = FundoInvestimento('data_files/zarathustra.csv', 'data_files/cdi.csv')
        self.assertEqual(fundo_zarathustra.maior_retorno_diario('2019-01-02', '2019-01-31'), result)

    def test_menor_retorno_diario(self):
        result = {'descricao': 'menor_retorno_diario', 'data': '2019-01-07', 'valor': -0.009555771613943387, 'valor_formatado': '-0,9556 %'}
        fundo_zarathustra = FundoInvestimento('data_files/zarathustra.csv', 'data_files/cdi.csv')
        self.assertEqual(fundo_zarathustra.menor_retorno_diario('2019-01-02', '2019-01-31'), result)
from io import BytesIO
import ptvsd
import pandas as pd

#Configuração do debbuger
ptvsd.enable_attach(address=('0.0.0.0', 5678), redirect_output=True)
ptvsd.wait_for_attach()


class SerieInvalida(Exception):
    """Serie de dados incompatível com as operações financeiras"""
    pass

class FundoInvestimento():
    """Classe global que avalia series de dados formatados relacionados a fundos de investimento"""
    def __init__(self, serie_dados_fundo, serie_dados_cdi):
        self.serie_dados_fundo = serie_dados_fundo
        self.serie_dados_cdi = serie_dados_cdi

print('funciona')
print('ok')

import pandas as pd
from planilhas import ContadorRepository
from usecase import UseCaseContador

class ContadorFactory:

    @staticmethod
    def start() -> UseCaseContador:
        try: 
            planilha = input('Qual o nome da planilha: ')
            planilha = pd.read_excel(f'{planilha}.xlsx')
            print(planilha)
            col = input('Qual coluna? ')
            linha = input('Qual linha? ')
            print(planilha.loc[planilha[f'{col}'==linha], f'{col}'].sum())
        except:
            print('Deu bosta')

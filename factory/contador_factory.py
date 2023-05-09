import pandas as pd
from planilhas import ContadorRepository
from usecase import UseCaseContador

class ContadorFactory:

    @staticmethod
    def start() -> UseCaseContador:
        try:
            planilha = input('Qual o nome da planilha? ')
            planilha = pd.read_excel(f'{planilha}.xlsx')
            print(planilha)
            # col = str(input('Qual coluna? '))
            soma = planilha[planilha['preço']].sum()
            print(soma)
        except Exception as error:
            print(f'deu esse erro ai, {error}')

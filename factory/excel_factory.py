from planilhas import ExcelRepository, AlterarExcelRepository
from usecase import UseCase, Funcionario
import openpyxl as op

class ExcelFactory:

    @staticmethod
    def create() -> UseCase:
        planilha = op.Workbook()
        pagina = planilha['Sheet']

        while True:
            informacoes = input('O que deseja adicionar?').split(';')
            pagina.append(informacoes)
            pergunta = input('Deseja continuar?').lower()

            if pergunta == 'n':
                break

        nome = input('Como vamos nomear sua planilha?')

        planilha.save(f'{nome}.xlsx')

        return UseCase(ExcelRepository.Create_sheet(planilha=planilha, informacoes=informacoes, nome=nome))
    
class AlterarFactory:

    @staticmethod
    def Alterar() -> Funcionario:
            try:
                planilha = input('Qual planilha: ')
                pagina = input('Qual pagina: ')
                planilha = op.load_workbook(f'{planilha}.xlsx')
                pagina = planilha[pagina]
                sub = input('O que quer mudar: ')
                o = input('Pelo que: ')
                for rows in pagina.iter_rows(min_row=1, max_row=1000):
                     for cell in rows:
                          if cell.value == sub:
                               cell.value = o
                planilha.save(f'{planilha}.xlsx')
                return Funcionario(AlterarExcelRepository.Alter_sheet(planilha=planilha, pagina=pagina,substituicao=sub, substituto=o))
            except Exception as error:
                print('Deu bosta', error)
            else:
                print('ai sim ein')
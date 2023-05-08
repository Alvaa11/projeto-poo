from interface import ExcelInterface, IAlterarExcel
from typing import Dict


class ExcelRepository(ExcelInterface):

        def Create_sheet(planilha, informacoes, nome):
              pass

class AlterarExcelRepository(IAlterarExcel):
       
       def Alter_sheet(planilha, substituicao, substituto,  pagina):
            pass
            
            
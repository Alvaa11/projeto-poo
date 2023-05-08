from abc import ABC, abstractmethod

class ExcelInterface(ABC):

    @abstractmethod
    def Create_sheet(planilha, informacoes, nome):
        planilha = planilha
        informacoes = [informacoes]
        nome = nome
        return

class IAlterarExcel(ABC):

    @abstractmethod
    def Alter_sheet(planilha, substituicao, substituto, pagina):
        planilha = planilha
        substituicao = substituicao
        substituto = substituto
        pagina = pagina
        return
from interface import IContador

class ContadorRepository(IContador):

    def Contar(planilha, col):
        super().Contar( col)
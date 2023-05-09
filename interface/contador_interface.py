from abc import ABC, abstractmethod

class IContador(ABC):

    @abstractmethod
    def Contar(planilha, col):
        pass
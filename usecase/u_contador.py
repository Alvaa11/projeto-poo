from planilhas import ContadorRepository
from typing import Type

class UseCaseContador:
    def __init__(self, repositorio: Type[ContadorRepository]) -> None:
        self.__repositorio = repositorio

    def do_something(self, data: bool) -> bool:
        if data is True:
            repositorio = self.__repositorio
            return repositorio
        return None
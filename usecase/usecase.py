from typing import Type, Union, Dict
from interface import ExcelInterface, IAlterarExcel

class UseCase:

    def __init__(self, repository: Type[ExcelInterface]) -> None:
        self.__repository = repository

    def do_something(self, data: bool) -> Union[None, Dict]:
        if data is True: 
            repositoryresponse = self.__repository
            return repositoryresponse
        else:
            return None
        
class Funcionario:
    def __init__(self, repository: Type[IAlterarExcel]) -> None:
        self.__repository = repository

    def fazer_algo(self, data: bool) -> Union[Dict, None]:
        if data is True:
            repository = self.__repository
            return repository
        else:
            return None
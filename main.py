from factory import ExcelFactory, AlterarFactory
import usecase

# usecase = ExcelFactory.create()
# response = usecase.do_something(True)

# print(response)

funcionario = AlterarFactory.Alterar()
response = funcionario.fazer_algo(True)


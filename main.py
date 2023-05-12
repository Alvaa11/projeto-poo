from factory import ExcelFactory, AlterarFactory
from avisos import linha

print(f"""
{linha()}
CRIAR PLANILHA | ALTERAR PLANILHA   
Digite "Criar"  Digite "Alterar"
para criar uma  para alterar uma
planilha        uma planilha
{linha()}
""")

service = str(input('Qual serviço deseja usar hoje: ')).capitalize()
if service == 'Criar':
    usecase = ExcelFactory.create()
elif service == 'Alterar':
    funcionario = AlterarFactory.Alterar()



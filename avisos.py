def linha():
    print('=-' * 50)

def boas_vindas_criar():
    print(f'''
{linha}
Seja bem-vindo! sou o criador de planilhas, tudo bem com você?
{linha}
''')

def aviso1():
    print(f'''
{linha}
AVISO:
{linha}
Adicionamos sempre valores por linhas, então começaremos na linha A1 okay?
e a cada vez que você der um enter para adicionar as informações
pularemos para a celula de baixo. Para adicionar valores as celulas
do lado digite ";" Por exemplo: Produto ; Preço (enter)
                                Nike ; R$500,00
''')
    
def boas_vindas_alterar():
    print(f'''
{linha}
Seja bem-vindo! sou o alterador de planilhas, tudo bem com você?
{linha}
''')

def aviso2():
    print(f'''
{linha}
AVISO:
{linha}
Você deve escrever o que deve ser substituido extamente como ele está escrito,
do contrário, nosso sistema não achará o que você deseja
''')
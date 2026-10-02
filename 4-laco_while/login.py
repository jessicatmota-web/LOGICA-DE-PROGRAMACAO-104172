import os
os.system('cls')


print('===CADASTRO===')

usuario = input('Crie seu usuário: ')
senha = input('Crie sua senha: ')

os.system('cls')

print('=== LOGIN ===')

login_usuario = input('Digite seu usuário: ')
login_senha = input('Digite sua senha: ')

while True:
    if login_usuario == usuario and login_senha == senha:
        print('Login realizado com sucesso!')
    else:
        print('Usuário ou senha incorretos!')

    login_usuario = input('Digite seu usuário: ')
    login_senha = input('Digite sua senha: ')

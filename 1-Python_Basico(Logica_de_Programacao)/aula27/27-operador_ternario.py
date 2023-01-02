"""
logged_user = True

if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar.'

print(msg)
"""
'''
logged_user = False
msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'


print(msg)
'''

idade = 18
e_de_maior = (idade >= 18)
msg = 'Pode acessar' if e_de_maior else 'Não pode acessar'

print(msg)

clientes = {
    'cliente1': {
      'nome': 'Willian',
        'sobrenome': 'Machado'
    },
    'cliente2': {
      'nome': 'Luiz',
        'sobrenome': 'Otávio'
    },
    'cliente3': {
      'nome': 'Suelen',
        'sobrenome': 'Campos'
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k}: {dados_v}')


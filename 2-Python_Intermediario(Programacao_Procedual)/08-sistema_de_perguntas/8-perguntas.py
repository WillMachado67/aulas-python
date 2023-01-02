print('Excolha uma alternativa entre A & D')
print()


perguntas = {
    'pergunta1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'A': '1', 'B': '4', 'C': '5', 'D': '0', },
        'resposta_certa': 'B',
    },
    'pergunta2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {'A': '5', 'B': '10', 'C': '6', 'D': '9', },
        'resposta_certa': 'C',
    },
    'pergunta3': {
        'pergunta': 'Quanto é 2*2? ',
        'respostas': {'A': '7', 'B': '1', 'C': '2', 'D': '4', },
        'resposta_certa': 'D',
    },
    'pergunta4': {
        'pergunta': 'Quanto é 3-2? ',
        'respostas': {'A': '1', 'B': '6', 'C': '3', 'D': '5', },
        'resposta_certa': 'A',
    },
    'pergunta5': {
        'pergunta': 'Quanto é 1+2? ',
        'respostas': {'A': '0', 'B': '3', 'C': '2', 'D': '4', },
        'resposta_certa': 'B',
    },
}
resposta_certa = 0

for pk, pv in perguntas.items():
    print(f"{pk}: {pv['pergunta']}")

    print('Repostas: ')
    for rk, rv in pv['respostas'].items():
        print(f"[{rk}]: {rv}")

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario.upper() == pv['resposta_certa']:
        print('Certa resposta!')
        resposta_certa += 1
    else:
        print('Você errou')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = resposta_certa / qtd_perguntas * 100

print(f'Você acertou {resposta_certa} resposras.')
print(f'Sua porcentagem de acertou foi de {porcentagem_acerto}%.')

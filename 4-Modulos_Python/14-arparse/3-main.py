# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá mundo" na tela',
    # type=str,
    metavar='STRING',
    # default='Olá mundo',
    # required=True,  # Obriga a inserir argumento
    # nargs='+',  # Recebe mais de um valor
    action='append'  # Recebe o argumento mais de uma vez
    )
args = parser.parse_args()

print(args.basic)

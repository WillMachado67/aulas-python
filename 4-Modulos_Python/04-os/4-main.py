# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os

caminho = os.path.join('/home', 'willian', 'Documentos',
                       '4-Modulos_Python', '4-os')

for root, dirs, files in os.walk(caminho):
    the_root = os.path.basename(root.upper())
    print('Pasta', the_root, root)

    for dir_ in dirs:
        print(' ', the_root, 'Dir:', dir_)

    for file_ in files:
        # caminho_completo = os.path.join(root, file_)
        print(' ', the_root, 'File:', file_)
        # os.unlink('Abrir Pasta reserva')

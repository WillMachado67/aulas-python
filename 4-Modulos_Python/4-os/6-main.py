# os.path.getsize e os.stat para dados dos arquivos (tamanho em bytes)
import os
from defmath import formata_tamanho


caminho = os.path.join('/home', 'willian', 'Documentos', 'Willian',
                       'Curso-Luiz_Otavio_Miranda', 'python/Aulas',
                       '4-Modulos_Python', '4-os')

for root, dirs, files in os.walk(caminho):
    the_root = os.path.basename(root.upper())
    print('Pasta', the_root, root)

    for dir_ in dirs:
        print(' ', the_root, 'Dir:', dir_)

    for file_ in files:
        caminho_completo = os.path.join(root, file_)
        stats = os.stat(caminho_completo)
        tamanho = stats.st_size
        tamanho_formatado = formata_tamanho(tamanho, tamanho_real=True)
        print(' ', the_root, 'File:', file_, tamanho_formatado)

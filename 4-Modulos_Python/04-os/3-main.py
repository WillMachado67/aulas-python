# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
import os

caminho = os.path.join('/home', 'willian', 'Documentos', 'Willian',
                       'Curso-Luiz_Otavio_Miranda', 'python/Aulas',
                       '4-Modulos_Python')

for pasta in os.listdir(caminho):
    print(pasta)
    for arquivo in os.listdir(pasta):
        print(' ', arquivo)

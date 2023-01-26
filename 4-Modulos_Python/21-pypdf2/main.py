# Documentação:
# https://pythonhosted.org/PyPDF2/
# Mais exemplos de uso:
# http://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/

# pip install pypdf2 # virtualenv
# pipenv install pypdf2 # pipenv
import PyPDF2
from pathlib import Path


CAMINHO_ROOT = Path(__file__).parent
CAMINHO_PDF = CAMINHO_ROOT / 'pdf'
CAMINHO_NOVO_PDF = CAMINHO_PDF / 'novo_arquivo.pdf'
CAMINHO_PDF_SEPARADO = CAMINHO_ROOT / 'pdf_separado'


# Junta os arquivos
novo_pdf = PyPDF2.PdfMerger()
for arquivo_pdf in CAMINHO_PDF.iterdir():
    arquivo = open(arquivo_pdf, 'rb')
    novo_pdf.append(arquivo)

with open(CAMINHO_NOVO_PDF, 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)


# # Separa o arquivo
# with open(CAMINHO_NOVO_PDF, 'rb') as arquivo_pdf:
#     leitor = PyPDF2.PdfReader(arquivo_pdf)
#     num_paginas = len(leitor.pages)
    
#     for num_pagina in range(num_paginas):
#         escritor = PyPDF2.PdfWriter()
#         pagina_atual = leitor.pages[num_pagina]
#         escritor.add_page(pagina_atual)

#         with open(CAMINHO_PDF_SEPARADO / f'{num_pagina}.pdf', 'wb') as novo_pdf:
#             escritor.write(novo_pdf)

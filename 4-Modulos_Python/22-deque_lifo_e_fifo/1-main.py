# Pilhas e filas
# Pilhas (stack) - LIFO - last in, first out.
#   Exepmplo: Pilhas de livros que sao adicionados um sobre o outro
# Fila (queue) - FIFO -frist in, frist out.
#   Exemplo: Uma fila de banco (ou qualquer outra fila da vida real)
#  Fila podem ter efeito colaterais em desempenho, porque a cada item alterado,
#   todos os índices serão modificados
livros: list = []
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')
livros.append('Livro 5')

livro_removido = livros.pop()  # 5
print(livros, livro_removido)
livro_removido = livros.pop()  # 4
print(livros, livro_removido)
livro_removido = livros.pop()  # 3
print(livros, livro_removido)
livro_removido = livros.pop()  # 2
print(livros, livro_removido)
livro_removido = livros.pop()  # 1

print(livros, livro_removido)

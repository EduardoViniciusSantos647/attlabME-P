
livros = []

for i in range(1, 4):
    titulo = input(f"Digite o título do {i}º livro mais emprestado: ")
    livros.append(titulo)

print("\nLivros cadastrados:")
for titulo in livros:
    print(titulo)

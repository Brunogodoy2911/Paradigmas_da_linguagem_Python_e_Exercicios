from classes.livro import Livro
from classes.biblioteca import Biblioteca

livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro2 = Livro("1984", "George Orwell", 1949)
livro3 = Livro("Dom Quixote", "Miguel de Cervantes", 1605)

lista_inicial = [livro1, livro2]
minha_biblioteca = Biblioteca("Biblioteca Pública Central", lista_inicial)

minha_biblioteca.listar_livros()

print("\nAdicionando um novo livro...\n")
minha_biblioteca.adicionar_livro(livro3)

minha_biblioteca.listar_livros()

print("\nRemovendo um livro...\n")
minha_biblioteca.remover_livro(livro2)

minha_biblioteca.listar_livros()

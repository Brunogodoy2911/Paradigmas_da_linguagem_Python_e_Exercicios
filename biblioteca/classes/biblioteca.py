class Biblioteca:
  def __init__(self, nome, livros):
    self.nome = nome
    self.livros = livros

  def adicionar_livro(self, livro):
    self.livros.append(livro)

  def remover_livro(self, livro):
    self.livros.remove(livro)

  def buscar_livro(self, titulo):
    for livro in self.livros:
      if livro == livro.titulo:
        return livro
      return None

  def listar_livros(self):
    print(f"--- Livros na Biblioteca: {self.nome} ---")
    for livro in self.livros:
      print(f"- Título: {livro.titulo}, Autor: {livro.autor}")
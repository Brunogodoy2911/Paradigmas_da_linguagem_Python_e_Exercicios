from datetime import date

class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  @classmethod
  def apartiranonasc(cls, nome, ano):
    return cls(nome, date.today().year - ano)
  
  @staticmethod
  def ehmaior(idade):
    return idade >= 18
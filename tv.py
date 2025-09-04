class Televisao:
  canal_sintonizado = 0
  numero_maior_canal = 0
  numero_menor_canal = 0

  def __init__(self, canal_inicial, maior_canal, menor_canal):
    self.canal_inicial = canal_inicial
    self.maior_canal = maior_canal
    self.menor_canal = menor_canal
    Televisao.canal_sintonizado += 1
    Televisao.numero_maior_canal = maior_canal
    Televisao.numero_menor_canal = menor_canal

  def aumentar_canal(self):
    if self.canal_sintonizado == self.maior_canal:
      self.canal_sintonizado = self.canal_inicial
    else:
      self.canal_sintonizado += 1
    
  def diminuir_canal(self):
    if self.canal_sintonizado == self.menor_canal:
      self.canal_sintonizado = self.maior_canal
    else:
      self.canal_sintonizado -= 1

  def imprimir_canal_sintonizado(self):
    print(f"Canal sintonizado: {self.canal_sintonizado}")

def main():
  tv1 = Televisao(0, 100, 0)

  tv1.aumentar_canal()
  tv1.imprimir_canal_sintonizado()
 
  tv1.diminuir_canal()
  tv1.imprimir_canal_sintonizado()

  tv1.diminuir_canal()
  tv1.imprimir_canal_sintonizado()

  tv1.diminuir_canal()
  tv1.imprimir_canal_sintonizado()

  tv1.imprimir_canal_sintonizado()

if __name__ == "__main__":
  main() 

#   class Televisao:
#     def __init__(self, pcanal, min, max):
#         self.canal = pcanal
#         self.cmin = min
#         self.cmax = max

#     def muda_canal_para_baixo(self):
#         self.canal -= 1


#     def muda_canal_para_cima(self):
#         self.canal += 1

# tv1 = Televisao(2 , 2,  10 )
# print(f"Canal Sintonizado: ",tv1.canal)

# print(f"Mudando canal para cima")
# for x in  range (1,20):
#     tv1.muda_canal_para_cima()
#     print(f"Canal Sintonizado: ",tv1.canal)

# tv2 = Televisao(10, 2, 10)
# print(f"Canal Sintonizado: ",tv2.canal)
# print(f"Mudando canal para baixo")
# for x in  range (1,20):
#     tv2.muda_canal_para_baixo()
#     print(f"Canal Sintonizado: ",tv2.canal)


     
    
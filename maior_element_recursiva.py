lista = [10, 20, 30, 50, 40]

def busca_recursiva(lista):
    if (len(lista) <= 1):
        return lista[0]
        
    primeiro_elemento = lista[0]
    
    maior_do_resto_da_lista = busca_recursiva(lista[1:])
    
    if primeiro_elemento > maior_do_resto_da_lista:
        return primeiro_elemento
    else:
        return maior_do_resto_da_lista
        
maior_valor = busca_recursiva(lista)
print(f"O maior elemento encontrado foi: {maior_valor}")
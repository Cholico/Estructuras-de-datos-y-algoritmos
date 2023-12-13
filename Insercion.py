from random import randint


def insercion(lista) -> list():
    for i in range(1, len(lista)):
       # Puesto que tomamos el primer valor como elemento ya ordenado nos pocisionamos en el segundo elemento y apartir de ahi analizamos
       valor_actual = lista[i]
       # Usamos esta variable para situarnos en la posicion que analizaremos
       posicion_actual = i

       while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
           lista[posicion_actual] = lista[posicion_actual-1]
           posicion_actual -= 1
        
       lista[posicion_actual] = valor_actual

    return lista

def main():
    catidad = randint(10, 20)
    lista = [randint(0 ,100) for i in range(catidad)]

    print("Lista desordenada: ")
    print(lista)
    print("Lista ordenada: ")
    print(insercion(lista))

main()
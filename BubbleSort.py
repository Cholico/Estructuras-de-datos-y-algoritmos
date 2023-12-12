from random import randint

def bubbleSort(lista) -> list():
    aux = int()
    vueltas = int(0)
    ordenado = bool(False)

    while(ordenado == False):
        ordenado = True
        for i in range(len(lista)-1-vueltas):
            if lista[i]  > lista[i+1]:
                aux = lista[i+1]
                lista[i+1] = lista[i]
                lista[i] = aux
                
                ordenado = False
        
        vueltas += 1

    return lista


def main():
    
    cantidad_aleatoria = randint(10,50)
    lista = [randint(0,100) for i in range(cantidad_aleatoria)]

    print("Lista desordenada: ")
    print(lista)

    print("Lista ordenada: ")
    print(bubbleSort(lista))


main()
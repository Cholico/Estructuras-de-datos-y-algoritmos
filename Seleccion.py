from random import randint


def seleccion(lista) -> list():
    longuitud = len(lista)

    for i in range(longuitud-1):
        # Suponemos que el primer elemento no ordenado es el mínimo
        min_index = i

        # Buscamos el elemento más pequeño en el resto del array
        for j in range(i+1, longuitud):
            if lista[j] < lista[min_index]:
                min_index = j

        # Intercambiamos el elemento más pequeño con el primer elemento no ordenado
        lista[i], lista[min_index] = lista[min_index], lista[i]

    return lista

def main():
    catidad = randint(10, 20)
    lista = [randint(0 ,100) for i in range(catidad)]

    print("Lista desordenada: ")
    print(lista)
    print("Lista ordenada: ")
    print(seleccion(lista))

main()
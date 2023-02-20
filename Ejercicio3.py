numero = int(input("Introduce un número: "))

palabras = []

for palabra in range(numero):
    Pusuario = input("Introduce una palabra: ")
    palabras.append(Pusuario)

print("Lista de palabras:", palabras)

Pnueva = input("Introduce una nueva palabra: ")

for palabra in range(int(len(palabras) / 2)):
    palabras[palabra] = Pnueva

print("Lista de palabras actualizadas:", palabras)

buscador = input("Introduce una palabra para saber si esta en la lista: ")

if buscador in palabras:
    print("La palabra está en la lista.")
else:
    print("La palabra no está en la lista.")

import random

Paleatoria = random.choice(palabras)

print("Una palabra aleatoria de la lista es:", Paleatoria)
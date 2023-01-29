nteclado=int(input("Dame un numero: "))
lista=[]

for i in range(nteclado):
    print("Dígame la palabra", str(i + 1), ": ",sep=" ",end="")
    palabra=input()
    lista+=[palabra]

print("La lista creada es:", lista) 

#Me falta la mitad del ejercicio 3

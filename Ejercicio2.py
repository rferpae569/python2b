from random import randrange
nteclado=int(input("Cuantos numeros quieres: "))

if nteclado<1:
    print("Fallo")
else:
    lista=[]
    for i in range(nteclado):
        numero=randrange(1,21)
        lista+=[numero]
print("Los numeros son: ",lista)
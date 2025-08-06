a=int(input("Posição do carro A:"))
b=int(input("Posição do carro B:"))
c=int(input("Posição do carro C:"))

if (b-a)<(c-b):
    print("1")
elif (b-a)>(c-b):
    print("-1")
else:
    print("0")

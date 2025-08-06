r=int(input("Resultado obtido pelo atleta:"))
m=int(input("Recorde mundial:"))
l=int(input("Recorde olímpico:"))

if r>m:
    print("RM")
else:
    print("*")
if r>l:
    print("RO")
else:
    print("*")

a = int(input("Nível do primeiro jogador:"))
b = int(input("Nível do segundo jogador:"))
c = int(input("Nível do quato jogador:"))
d = int(input("Nível do quinto jogador:"))

if (a+d)<(b+c):
    x=(b+c)-(a+d)
    print(f"A diferença dos níveis é de {x}")
else:
    x=(a+d)-(b+c)
    print(f"A diferença dos níveis é de {x}")
total = 0
primeira_nota = True
nota = float(input('Nota:'))

while nota >= 0:
    if primeira_nota:
         maior = nota
         menor = nota
         primeira_nota = False
    elif nota > maior:
         maior = nota
    elif nota < menor:
         menor = nota
    total = total + 1
    nota = float(input('Nota:'))

if total > 0:
     print(f'Total: {total}')
     print(f'Maior nota: {maior}')
     print(f'Menor nota: {menor}')
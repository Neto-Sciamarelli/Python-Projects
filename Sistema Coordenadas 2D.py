#Plano Cartesiano com origem translada

import math as mt

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
n = int(input("Digite quantos pontos deseja ter: "))
maior = 0 
maiorP = 0

for i in range(n):
    x1 = int(input("Digite o x do ponto: "))
    y1 = int(input("Digite o y do ponto: "))
    d = mt.sqrt(mt.pow(x1-x, 2) + mt.pow(y1-y, 2))
    ponto = (x1,y1)
    menor = d
    menorP = ponto
    
    if x1 == x:
        quadrante = "Está no eixo y"
    elif y1 == y:
        quadrante = "Está no eixo x"
    elif x1 == x and y1 == y:
        quadrante = "Está na origem"
    else:
        if (x1 - x) > 0 and (y1 - y) > 0:
            quadrante = "Está no primeiro quadrante"
        elif (x1 - x) < 0 and (y1 - y) > 0:
            quadrante = "Está no segundo quadrante"
        elif(x1 - x) < 0 and (y1 - y) < 0:
            quadrante = "Está no terceiro quadrante"
        elif(x1 - x) > 0 and (y1 - y) < 0:
            quadrante = "Está no quarto quadrante"
    print("O ponto", ponto, quadrante)

    if d > maior:
        maior = d
        maiorP = ponto
    elif d < menor:
        menor = d
        menorP = ponto

print("========================================")   
print("O ponto", menorP, "está mais próximo, a distancia é: {:.2f}" .format(menor))
print("O ponto", maiorP, "está mais distante, a distancia é: {:.2f}" .format(maior))
print("Fim do programa!")



    
    
print("="*30)
print("CADASTRO DE PESSOA FÍSICA!")
print("="*30)

num = int(input("Quantas pessoas deseja cadastrar: "))

for i in range(num):
    nome = input("Digite o nome: ")
    nome = nome.upper()
    idade = int(input("Digite a idade: "))
    nacio = input("Digite a nacionalidade: ")
    nacio = nacio.upper()
    registro = int(input("Digite o registro civil: "))
    print("")

    with open("cadastro.txt", "a") as arquivo:
        print("\nNome: "+nome, file = arquivo)
        print("Idade:",idade,  file = arquivo)
        print("Nacionalidade: "+nacio, file = arquivo)
        print("Refistro Civil:",registro , file = arquivo)
    











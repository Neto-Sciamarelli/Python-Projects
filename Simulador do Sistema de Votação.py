pres = []
gov = []
pref = []
eleitores = []
partidos = []
votoBrancoPref = 0
votoBrancoGov = 0
votoBrancoPres = 0
votoNuloPref = 0
votoNuloGov = 0
votoNuloPres = 0
totalVotos = 0

def menu():
    print("MENU - SIMULADOR DO SISTEMA DE VOTAÇÃO")
    print("1. Cadastrar Candidatos")
    print("2. Cadastrar Eleitores")
    print("3. Votar")
    print("4. Apurar Resultados")
    print("5. Relatório e Estatísticas")
    print("6. Encerrar")
    op = int(input("Opção escolhida: "))

    if op == 1:
        print("")
        cadastrarCand()
    elif op == 2:
        print("")
        cadastrarElei()
    elif op == 3:
        print("")
        votar()
    elif op == 4:
        print("")
        apurarResultado()
    elif op == 5:
        print("")
        relatorio()
    else:
        print("")
        print("FIM DO PROGRAMA!")   

def cadastrarCand():
    while True:
        cargo = input("Digite o cargo a ser disputado: ")
        print("")
        if cargo == "prefeito":
            nome = input("Digite o nome do candidato: ")
            num = int(input("Digite o número do candidato: "))
            part = input("Digite o partido do candidato: ")
            voto = 0
            lst = [nome, num, part, cargo, voto]
            pref.append(lst)
        elif cargo == "governador":
            nome = input("Digite o nome do candidato: ")
            num = int(input("Digite o número do candidato: "))
            part = input("Digite o partido do candidato: ")
            voto = 0
            lst = [nome, num, part, cargo, voto]
            gov.append(lst)
            if part not in partidos:
                partidos.append(part)
        elif cargo == "presidente":
            nome = input("Digite o nome do candidato: ")
            num = int(input("Digite o número do candidato: "))
            part = input("Digite o partido do candidato: ")
            voto = 0
            lst = [nome, num, part, cargo, voto]
            pres.append(lst)
        print("")
        op = input("Deseja cadastrar outro candidato? ")
        if op == "sim":
            print("")
            continue
        else:
            print("")
            menu()
            break

def cadastrarElei():
    while True:
        nome = input("Digite o nome do eleitor: ")
        cpf = int(input("Digite o CPF do eleitor: "))
        lst = [nome, cpf]
        eleitores.append(lst)
        print("")
        op = input("Deseja cadastrar outro eleitor? ")
        if op == "sim":
            print("")
            continue
        else:
            print("")
            menu()
            break

def votar():
    cont = 1
    while cont <= len(eleitores):
        num = int(input("Digite o número do seu candidato a prefeito: "))
        if num == -1:
            print("")
            x = input("Vc está votando em branco, tem certeza? ")
            if x == "sim":
                global votoBrancoPref
                votoBrancoPref += 1
        elif num == -2:
            global votoNuloPref
            votoNuloPref += 1
        print("")
        for i in range(len(pref)):
            for j in range(len(pref[i])):
                if num == pref[i][j]:
                    print("O seu candidato: ", pref[i][0], pref[i][1], pref[i][2], pref[i][3])
                    op = input("Deseja confirmar seu voto? ")
                    if op == "sim":
                        pref[i][4] += 1
                    else:
                        print("")
                        menu()
                        break
                else:
                    continue
        print("")
        num2 = int(input("Digite o número do seu candidato a governador: "))
        if num2 == -1:
            x = input("Vc está votando em branco, tem certeza? ")
            if x == "sim":
                global votoBrancoGov
                votoBrancoGov += 1
        elif num2 == -2:
            global votoNuloGov
            votoNuloGov += 1
        for i in range(len(gov)):
            for j in range(len(gov[i])):
                if num2 == gov[i][j]:
                    print("O seu candidato: ", gov[i][0], gov[i][1], gov[i][2], gov[i][3])
                    op2 = input("Dseja confirmar seu voto? ")
                    if op2 == "sim":
                        gov[i][4] += 1
                    else:
                        print("")
                        menu()
                        break
                else:
                    continue
        print("")
        num3 = int(input("Digite o número do seu candidato a presidente: "))
        if num3 == -1:
            x = input("Vc está votando em branco, tem certeza? ")
            if x == "sim":
                global votoBrancoPres
                votoBrancoPres += 1
        elif num3 == -2:
            global votoNuloPres
            votoNuloPres += 1
        for i in range(len(pres)):
            for j in range(len(pres[i])):
                if num3 == pres[i][j]:
                    print("O seu candidato: ", pres[i][0], pres[i][1], pres[i][2], pres[i][3])
                    op3 = input("Deseja confirmar seu voto? ")
                    if op3 == "sim":
                        pres[i][4] += 1
                    else:
                        print("")
                        menu()
                        break
        cont += 1
        print("")
    print("")
    menu()

def apurarResultado():
    totalVotos = len(eleitores)
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(len(pref)-1):
            if pref[i][4] > pref[i+1][4]:
                pref[i], pref[i+1] = pref[i+1], pref[i]
                ordenado = False 
    
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(len(gov)-1):
            if gov[i][4] > gov[i+1][4]:
                gov[i], gov[i+1] = gov[i+1], gov[i]
                ordenado = False 
    
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(len(pres)-1):
            if pres[i][4] > pres[i+1][4]:
                pres[i], pres[i+1] = pres[i+1], pres[i]
                ordenado = False 

    pref.reverse()
    gov.reverse()
    pres.reverse()

    partidos.append(pref[0][2])
    partidos.append(gov[0][2])
    partidos.append(pres[0][2])
    
    print("RANKING DO RESULTADO PARA PRESIDENTE")
    num = 1
    for i in range(len(pres)):
        print(num,".", pres[i][0], pres[i][2], pres[i][4],"/%.2f" %((pres[i][4]/totalVotos)*100),"%")
        num += 1
    votosValidos = totalVotos - votoBrancoPres - votoNuloPres
    print("Total de Votos: ",totalVotos)
    print("Votos Válidos:",votosValidos,"/%.2f" %((votosValidos/totalVotos)*100),"%")
    print("Votos Brancos: ",votoBrancoPres,"/%.2f" %((votoBrancoPres/totalVotos)*100),"%")
    print("Votos Nulo: ",votoNuloPres,"/%.2f" %((votoNuloPres/totalVotos)*100),"%")

    print("")
    print("RANKING DO RESULTADO PARA GOVERNADOR")
    num = 1
    for i in range(len(gov)):
        print(num,".", gov[i][0], gov[i][2], gov[i][4],"/%.2f" %((gov[i][4]/totalVotos)*100),"%")
        num += 1
    votosValidos = totalVotos - votoBrancoGov - votoNuloGov
    print("Total de Votos: ",totalVotos)
    print("Votos Válidos:",votosValidos,"/%.2f" %((votosValidos/totalVotos)*100),"%")
    print("Votos Brancos: ",votoBrancoGov,"/%.2f" %((votoBrancoGov/totalVotos)*100),"%")
    print("Votos Nulo: ",votoNuloGov,"/%.2f" %((votoNuloGov/totalVotos)*100),"%")

    print("")
    print("RANKING DO RESULTADO PARA PREFEITO")
    num = 1
    for i in range(len(pref)):
        print(num,".", pref[i][0], pref[i][2], pref[i][4],"/%.2f" %((pref[i][4]/totalVotos)*100),"%")
        num += 1
    votosValidos = totalVotos - votoBrancoPref - votoNuloPref
    print("Total de Votos: ",totalVotos)
    print("Votos Válidos:",votosValidos,"/%.2f" %((votosValidos/totalVotos)*100),"%")
    print("Votos Brancos: ",votoBrancoPref,"/%.2f" %((votoBrancoPref/totalVotos)*100),"%")
    print("Votos Nulo: ",votoNuloPref,"/%.2f" %((votoNuloPref/totalVotos)*100),"%")

    print("")
    op = int(input("Digite 1 para voltar ao Menu: "))
    if op == 1:
        print("")
        menu()

def relatorio():
    totalVotos = len(eleitores)
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(len(eleitores)-1):
            if eleitores[i][0] > eleitores[i+1][0]:
                eleitores[i], eleitores[i+1] = eleitores[i+1], eleitores[i]
                ordenado = False 

    print("LISTA DE ELEITORES")
    num = 1
    for i in range(len(eleitores)):
        print(num,".",eleitores[i][0])
        num += 1

    print("")

    print("AUDITORIA")
    if totalVotos == len(eleitores):
        print("O número de eleitores bate com o total de votos!")
    else:
        print("Há uma falha na contagem dos votos!")

    print("")

    if partidos.count(partidos[0]) == 2:
        print("O partido",partidos[0],"foi o que mais elegeu candidatos!")
    elif partidos.count(partidos[0]) == 1:
        print("O partido",partidos[0],"foi o que menos elegeu candidatos!")
    elif partidos.count(partidos[0]) == 3:
        print("O partido",partidos[0],"elegeu todos os seus candidatos")
    elif partidos.count(partidos[1]) == 2:
        print("O partido",partidos[1],"foi o que mais elegeu candidatos!")
    elif partidos.count(partidos[1]) == 1:
        print("O partido",partidos[1],"foi o que menos elegeu candidatos!")
    elif partidos.count(partidos[1]) == 3:
        print("O partido",partidos[1],"elegeu todos os seus candidatos")
    elif partidos.count(partidos[2]) == 2:
        print("O partido",partidos[2],"foi o que mais elegeu candidatos!")
    elif partidos.count(partidos[2]) == 1:
        print("O partido",partidos[2],"foi o que menos elegeu candidatos!")
    elif partidos.count(partidos[2]) == 3:
        print("O partido",partidos[2],"elegeu todos os seus candidatos")
    
    print("")

    op = int(input("Digite 1 para voltar ao Menu: "))
    if op == 1:
        print("")
        menu()
    
menu()
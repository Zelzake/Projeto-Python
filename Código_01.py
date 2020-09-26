def imprimemenu():
    print("-------------------")
    print("| 1) Iniciar jogo |")
    print("-------------------")
    print("| 2) Créditos     |")
    print("-------------------")
    print("| 3) Sair         |")
    print("-------------------")
    return "Escolha uma das opções: "


def vivo(saude, dinheiro, v_social, fama):
    if saude < 1 or dinheiro < 1 or v_social < 1 or fama < 1:
        print("Você perdeu!")
        exit()
    else:
        return ""


def iniciajogo():

    saude = 10
    dinheiro = 10
    v_social = 10
    fama = 10

    print("\n||  Tente sobreviver até o fim do mês sem que nenhum dos status chegue a 0 e junte 10 Dinheiros para pagar o aluguel ||")
    print("\n         Saude:", saude, "| Dinheiro:", dinheiro, "| Vida Social:", v_social, "| Fama:", fama)

    # level-1
    print("\nSeu patrão precisa apressar a entrega da próxima atualização de um App e te pede para trabalhar mais. Você trabalha as horas extras?\n1) SIM     2-9) NÂO")
    escolha = int(input("Sua escolha vai ser:\n"))
    if escolha == 1:
        dinheiro += 3
        v_social -= 5
        print("\nVocê trabalha algumas horas extras e ganha um pouco mais de dinheiro")
        print("Dinheiro +3 | Vida Social -2")
        print("\nSeus status: | Saude:", saude, "| Dinheiro:", dinheiro, "| Vida Social:", v_social, "| Fama:", fama)
        vivo(saude, dinheiro, v_social, fama)
    else:
        dinheiro -= 1
        fama -= 2
        v_social += 2
        print("\nVocê decide ficar em casa")
        print("Dinheiro -1 | Fama - 2 | Vida Social + 2")
        print("\nSeus status: | Saude:", saude, "| Dinheiro:", dinheiro, "| Vida Social:", v_social, "| Fama:", fama)
        vivo(saude, dinheiro, v_social, fama)

    # level-2
    print("\nSeu amigos te chama para almoçar em um restaurante chique. Você aceita?\n1) SIM     2-9) NÂO")
    escolha = int(input("Sua escolha vai ser:\n"))
    if escolha == 1:
        dinheiro -= 5
        saude += 2
        v_social += 4
        fama += 2
        print("\nVocê almoça com seus amigos, mas a conta acaba ficando um pouco mais cara do que você esperava")
        print("Dinheiro -5 | Saude + 2 | Vida Social + 4 | Fama + 2")
        print("\nSeus status: | Saude:", saude, "| Dinheiro:", dinheiro, "| Vida Social:", v_social, "| Fama:", fama)
        vivo(saude, dinheiro, v_social, fama)
    else:
        dinheiro += 2
        fama -= 2
        v_social -= 6
        print("\nVocê decide ficar em casa e desaponta seus amigos, mas economiza um pouco de dinheiro")
        print("Dinheiro + 2 | Fama - 2 | Vida Social -6")
        print("\nSeus status: | Saude:", saude, "| Dinheiro:", dinheiro, "| Vida Social:", v_social, "| Fama:", fama)
        vivo(saude, dinheiro, v_social, fama)

    # level-3
    print("\nUma academia abre perto de onde você mora. Você quer participar?\n1) SIM     2-9) NÂO")
    escolha = int(input("Sua escolha vai ser:\n"))
    if escolha == 1:
        dinheiro -= 3
        saude -= 1
        v_social += 5
        fama += 6
        print("\nVocê malha para ficar monstrão, mas acaba exagerando e machuca o trapézio descendente")
        print("Dinheiro -3 | Saude - 1 | Vida Social + 5 | Fama + 6")
        print("\nSeus status: | Saude:", saude, "| Dinheiro:", dinheiro, "| Vida Social:", v_social, "| Fama:", fama)
        vivo(saude, dinheiro, v_social, fama)
    else:
        dinheiro += 2
        v_social -= 3
        print("\nVocê prefere economizar um pouco de dinheiro e não ir na academia")
        print("Dinheiro + 2 | Vida Social - 3")
        print("\nSeus status: | Saude:", saude, "| Dinheiro:", dinheiro, "| Vida Social:", v_social, "| Fama:", fama)
        vivo(saude, dinheiro, v_social, fama)

    # level-4
    print("\nVocê ouve falar que um novo filme da Marvel está nos cinemas. Pretende ir?\n1) SIM     2-9) NÂO")
    escolha = int(input("Sua escolha vai ser:\n"))
    if escolha == 1:
        dinheiro -= 3
        v_social += 2
        print("\nVocê vê o novo filme da Marvel, mas não gosta tanto por que tinha um cara gritando'Os quadrinhos eram melhores' no banco da frente")
        print("Dinheiro -1 | Vida Social + 2")
        print("\nSeus status: | Saude:", saude, "| Dinheiro:", dinheiro, "| Vida Social:", v_social, "| Fama:", fama)
        vivo(saude, dinheiro, v_social, fama)
    else:
        dinheiro += 3
        saude += 5
        fama -= 7
        print("\nVocê decide dar uma volta no parque e não ver o filme. Algumas crianças caçoam de você, mas você encontra umas notas no chão e pega para você")
        print("Dinheiro + 3 | fama - 7 | Saúde +5")
        print("\nSeus status: | Saude:", saude, "| Dinheiro:", dinheiro, "| Vida Social:", v_social, "| Fama:", fama)
        vivo(saude, dinheiro, v_social, fama)

    # level-5
    print("\nUm dia seu carro não liga e você precisa ir ao emprego. Você aluga um taxi ou vai de bicicleta?\n"
          "1) TAXI     2-9) BICICLETA")
    escolha = int(input("Sua escolha vai ser:\n"))
    if escolha == 1:
        dinheiro -= 4
        v_social += 2
        fama += 8
        print("\nA viagem fica um pouco cara, mas seu chefe e seus amigos te elogiam por ainda chegar a tempo")
        print("Dinheiro -4 | Saude - 1 | Vida Social + 4 | Fama + 6")
        print("\nSeus status: | Saude:", saude, "| Dinheiro:", dinheiro, "| Vida Social:", v_social, "| Fama:", fama)
        vivo(saude, dinheiro, v_social, fama)
    else:
        dinheiro += 1
        v_social -= 2
        print("\nVocê salva um pouco de dinheiro, mas seus amigos percebem que você está um pouco suado")
        print("Dinheiro + 1 | Vida Social - 3")
        print("\nSeus status: | Saude:", saude, "| Dinheiro:", dinheiro, "| Vida Social:", v_social, "| Fama:", fama)
        vivo(saude, dinheiro, v_social, fama)

    # level-6
    print("\nUma empresa rival te oferece um salário maior. Você aceita?\n1) SIM     2-9) NÂO")
    escolha = int(input("Sua escolha vai ser:\n"))
    if escolha == 1:
        dinheiro += 7
        v_social -= 4
        fama -= 8
        print("\nVocê aceita o emprego na empresa rival, mas seus amigos ficaram decepcionados")
        print("Dinheiro +7 | Vida Social - 4 | Fama - 8")
        print("\nSeus status: | Saude:", saude, "| Dinheiro:", dinheiro, "| Vida Social:", v_social, "| Fama:", fama)
        vivo(saude, dinheiro, v_social, fama)
    else:
        dinheiro += 2
        v_social += 3
        fama += 8
        print("\nVocê decide não ir para a empresa rival. Seu chefe te dá um aumento e seus amigos se orgulham")
        print("Dinheiro + 2 | Vida Social + 3 | Fama + 8")
        print("\nSeus status: | Saude:", saude, "| Dinheiro:", dinheiro, "| Vida Social:", v_social, "| Fama:", fama)
        vivo(saude, dinheiro, v_social, fama)

    # Dia do aluguel
    print("\n\n--------------------------------------------------------------")
    print("Chega o dia de pagar o aluguel e o cobrador vem bater na sua porta.")
    escolha = int(input("\nO que você faz?\n"
    "1) Paga o aluguel (Dinheiro >= 15)\n"
    "2) Foge pela janela (Saúde >= 10)\n"
    "3) Inventa uma desculpa e pede um prazo maior (Fama >= 10)\n"
    "4-9) Nenhuma das anteriores\n"))

    if escolha == 1:
        if dinheiro >= 15:
            print("Você paga o aluguel\n     VOCÊ VENCEU!!")
            exit()
        else:
            print("Você não possui dinheiro o suficiente\n     VOCÊ PERDEU!!")
            exit()
    elif escolha == 2:
        if saude >= 10:
            print("Você dá um backflip pela janela e foge da cidade\n     VOCÊ VENCEU(eu acho)")
            exit()
        else:
            print("Você tenta pular pela janela mas acaba se cortando e indo parar no hospital\n     VOCÊ PERDEU!!")
            exit()
    elif escolha == 3:
        if fama >= 10:
            print("Você tem uma reputação confiável e o cobrador te dá um tempo extra\n     VOCÊ VENCEU!!")
            exit()
        else:
            print("Você tenta enganar o cobrador, mas ele fica bravo e te expulsa da casa\n VOCÊ PERDEU!!")
            exit()
    else:
        print("Você não tem dinheiro para pagar o aluguel e é despejado da casa\n     VOCÊ PERDEU!!")
        exit()


def mostracreditos():
    print("Esse jogo foi feito por:\nGuilherme José de Almeida")


def main():
    escolha = int(input(imprimemenu()))

    if escolha == 1:
        iniciajogo()

    elif escolha == 2:
        mostracreditos()

    elif escolha == 3:
        return 0

    else:
        if __name__ == '__main__':
            main()


main()

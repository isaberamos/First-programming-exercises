def usuario_escolhe_jogada(n, m):
    print()
    while True:
        num = int(input("Quantas peças você quer tirar? "))
        if num > m or (n - num) < 0:
            print()
            print("Ops! Jogada inválida. Tente novamente.")
            print()
        else:
            if num < 2:
                print("Você tirou uma peça.")
            else:
                print(f"Voce tirou {num} peças.")
            return num

def multiplo(n, m):
    achou = False
    if(n % (m+1)) == 0:
        achou = True
    return achou

def computador_escolhe_jogada(n, m):
    print()
    qtd = 0
    if n <= m:
        qtd =  n
    else:
        if multiplo(n, m):
            qtd = m
        else:
            pc = 0
            while pc % (m + 1) != n % (m + 1):
                pc = pc + 1
                if pc % (m + 1) == n % (m + 1):
                    qtd = pc
                    break
    if qtd < 2:
        print("O computador tirou uma peça.")
    else:
        print(f"O computador tirou {qtd} peças.")
    return qtd

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if multiplo(n, m):
        print()
        print("Voce começa!")
        jogador = 1
    else:
        print()
        print("Computador começa!")
        jogador = 0

    while n > 0:

        if jogador == 0:
            n = n - computador_escolhe_jogada(n, m)
            jogador = 1
        else:
            n = n - usuario_escolhe_jogada(n, m)
            jogador = 0
        if n == 0 and jogador == 0:
            print("Fim do jogo! Você ganhou!")
            break
        elif n == 0 and jogador == 1:
            print("Fim do jogo! O computador ganhou!")
            break

        if n < 2:
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            print(f"Agora restam {n }peças no tabuleiro.")

def campeonato():
    print("\nVoce escolheu um campeonato!\n")
    rodada = 1
    while rodada <= 3:
        print("**** Rodada",rodada,"****")
        print()
        partida()
        print()
        rodada = rodada + 1
    print("**** Final do campeonato! ****\n")
    print("Placar: Você 0 X",(rodada-1),"Computador")

print("Bem-vindo ao jogo do NIM! Escolha:\n")
op = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
if op == 1:
    print("\nVoce escolheu uma partida isolada\n")
    partida()
elif op == 2:
    campeonato()
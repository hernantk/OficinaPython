def teste():
    maoroyal=[(9,"D"),(10,"D"),(11,"D"),(12,"D"),(13,"D")]
    maostra=[(4,"D"),(6,"D"),(5,"D"),(7,"D"),(8,"D")]
    maoquadra=[(4,"D"),(4,"C"),(4,"H"),(4,"S"),(8,"D")]
    maofullhouse=[(4,"D"),(4,"C"),(4,"H"),(8,"S"),(8,"D")]
    maoflush=[(2,"D"),(5,"D"),(6,"D"),(7,"D"),(8,"D")]
    maostraight=[(3,"H"),(2,"H"),(6,"D"),(5,"D"),(4,"D")]
    maotrinca=[(3,"H"),(3,"D"),(3,"G"),(5,"D"),(4,"D")]
    maodoispares=[(3,"H"),(3,"D"),(4,"G"),(4,"D"),(8,"D")]
    maopar=[(3,"H"),(3,"D"),(5,"G"),(9,"D"),(8,"D")]
    maocartaalta=[(3,"H"),(11,"D"),(5,"G"),(9,"D"),(8,"D")]
    cartaal1 = [["5", "D"], ["8", "C"], ["9", "S"], ["T", "S"], ["A", "C"]]
    cartaal2 = [["2", "C"], ["5", "C"], ["7", "D"], ["8", "S"], ["Q", "H"]]
    pardamas1 = [["4", "D"], ["6", "S"], ["9", "H"], ["Q", "H"], ["Q", "D"]]
    pardamas2 = [["3", "D"], ["6", "D"], ["7", "H"], ["Q", "D"], ["Q", "S"]]
    fullhouse1 = [["2", "H"], ["2", "D"], ["4", "C"], ["4", "D"], ["4", "S"]]
    fullhouse2 = [["3", "C"], ["3", "D"], ["3", "S"], ["9", "S"], ["9", "D"]]
def descobrirmao(maoteste):
    c=0
    royalflush = False
    straightflush = False
    quadra = False
    fullhouse = False
    flush = False
    straight = False
    trinca = False
    doispares = False
    par = False
    cartaalta = False
    if maoteste[0][1] == maoteste[1][1] == maoteste[2][1] == maoteste[3][1] == maoteste[4][1]:
        if maoteste[0][0] == 9 and maoteste[1][0] == 10 and maoteste[2][0] == 11 and maoteste[3][0] == 12 and \
                maoteste[4][0] == 13:
            royalflush = True

        if royalflush == False:
            for i in range(4):
                if (maoteste[i + 1][0] - maoteste[i][0]) == 1:
                    c += 1
                    if c == 4:
                        straightflush = True
                else:
                    flush = True

    if flush == False:

        for i in range(4):
            if maoteste[i][0] == maoteste[i + 1][0]:
                c += 1

                valormao=maoteste[i][1]
                valormao1=maoteste[i+1][1]
        if c == 3 and (maoteste[3][0] != maoteste[4][0] or maoteste[0][0] != maoteste[1][0]):
            quadra = True
        elif c == 3:
            fullhouse = True

        elif c == 2:
            if (maoteste[2][0] != maoteste[3][0] and maoteste[3][0] != maoteste[4][0]) or (
                    maoteste[0][0] != maoteste[1][0] and maoteste[1][0] != maoteste[2][0]):
                trinca = True
        if c == 2:
            doispares = True

        elif c == 1:
            par = True

    if (trinca == False and royalflush == False and flush == False):
        for i in range(4):
            if (maoteste[i + 1][0] - maoteste[i][0]) == 1:
                c += 1
                if c == 4:
                    straight = True
            else:
                cartaalta = True

    if straightflush == True:
        valor = 10
    elif royalflush == True:
        valor = 9
    elif quadra == True:
        valor = 8
    elif fullhouse == True:
        valor = 7,maoteste[2][0]
    elif flush == True:
        valor = 6,maoteste[0][1]
    elif straight == True:
        valor = 5
    elif trinca == True:
        valor = 4
    elif doispares == True:
        valor = 3
    elif par == True:
        valor = 2,valormao,valormao1
    elif cartaalta == True:
        valor = 1,maoteste[4][0]
    return valor
def converterletpnume(maoteste):
    for carta in maoteste:
        if carta[0] == "T":
            carta[0] = 11
        elif carta[0] == "K":
            carta[0] = 12
        elif carta[0] == "Q":
            carta[0] = 13
        elif carta[0] == "A":
            carta[0] = 14
        else:
            carta[0] = int(carta[0])
        if carta[1]=="S":
            carta[1]=1
        elif carta[1]=="H":
            carta[1]=2
        elif carta[1]=="D":
            carta[1]=3
        elif carta[1]=="C":
            carta[1]=4

    return maoteste
def inserirmaojogador(maojoga):
    for mao in range(5):
        carta = input("Insira a carta %dº" % (mao + 1)).upper()
        naipe = input("Insira o Naipe da carta").upper()
        maojoga.append([carta, naipe])
conversor={1:"Carta Alta",2:"Par",3:"Dois Pares",
          4:"Trinca",5:"Straight",6:"Flush",
          7:"Full House",8:"Quadra",9:"Straight Flush",
          10:"Royal Flush"}




maojoga1=[]
maojoga2=[]



#print("Jogador 1")
#inserirmaojogador(maojoga1)
#print("Jogador 2")
#inserirmaojogador(maojoga2)



maox=converterletpnume(pardamas1)
maoy=converterletpnume(pardamas2)


maox=sorted(maox)
maoy=sorted(maoy)
print(maox)
print(maoy)

mao1=descobrirmao(maox)
mao2=descobrirmao(maoy)
print(mao1)
print(mao2)
if mao1>mao2:
    print("O jogador 1 Ganhou por "+conversor[mao1[0]])
else:
    print("O jogador 2 Ganhou por "+conversor[mao2[0]])





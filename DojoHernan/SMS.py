
conversor = {"A": "2", "B": "22", "C": "222", "D": "3", "E": "33", "F": "333", "G": "4", "H": "44", "I": "444",
             "J": "5", "K": "55", "L": "555", "M": "6", "N": "66", "O": "666",
             "P": "7", "Q": "77", "R": "777", "S": "7777", "T": "8", "U": "88", "V": "888", "W": "9", "X": "99",
             "Y": "999", "Z": "9999"," ":"0"}

palavra = " "

X = 0
c=0
texto = (input("Digite uma frase ")).upper()

letras = list(texto)

tamanholetras=(len(letras))

for i in range(tamanholetras):

    if letras[i] in conversor:
        adicionar=(conversor[letras[i]])
        if (palavra[int((len(palavra))-1)])==adicionar[0]:
            palavra+="_"
        palavra+=(adicionar)



print("Para escrever a palavra digite "+palavra)




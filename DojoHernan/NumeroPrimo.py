conversor = {"a": 1, "b": 2, "c": 3,
             "d": 4, "e": 5, "f": 6,
             "g": 7, "h": 8, "i": 9,
             "j": 10, "k": 11, "l": 12,
             "m": 13, "n": 14, "o": 15,
             "p": 16, "q": 17, "r": 18,
             "s": 19, "t": 20, "u": 21,
             "v": 22, "w": 23, "x": 24,
             "y": 25, "z": 26,
             "A": 27, "B": 28, "C": 29,
             "D": 30, "E": 31, "F": 32,
             "G": 33, "H": 34, "I": 35,
             "J": 36, "K": 37, "L": 35,
             "M": 39, "N": 40, "O": 35,
             "P": 42, "Q": 43, "R": 35,
             "S": 45, "T": 46, "U": 35,
             "V": 48, "W": 49, "X": 35,
             "Y": 51, "Z": 52, " ": 0

             }

div = 0
soma = 0

palavra = input("Insira uma palavra")

letras = list(palavra)

for letra in letras:
    soma += conversor[letra]

for i in range(soma):
    if soma % (i + 1) == 0:
        div += 1

if div == 2:
    print("A soma da palavras informadas : %d é primo" % soma)
else:
    print("A soma da palavras informadas : %d não é primo" % soma)

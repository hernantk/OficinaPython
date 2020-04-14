conversor = {"1": "I", "2": "II", "3": "III",
             "4": "IV", "5": "V", "6": "VI",
             "7": "VII", "8": "VIII", "9": "IX",
             "10": "X", "20": "XX", "30": "XXX",
             "40": "XL", "50": "L", "60": "LX",
             "70": "LXX", "80": "LXXX", "90": "XC",
             "100": "C", "200": "CC", "300": "CCC",
             "400": "CD", "500": "D", "600": "DC",
             "700": "DCC", "800": "DCCC", "900": "CM",

             "1000": "M", "2000": "MM", "3000": "MMM",
             "4000": "MMMM", "5000": "_V", "6000": "_VI",
             "7000": "_VII", "8000": "_VIII", "9000": "_IX",
             "0": ""
             }

numeroinserido = input("Insira um numero")
romano = ""
listanumero = list(numeroinserido)
numepos0 = int(listanumero[0])
tamanhonumero = int(len(listanumero))

if len(listanumero) == 2:

    listanumero[0] = str(numepos0 * 10)

elif len(listanumero) == 3:

    numpos1 = int(listanumero[1])
    listanumero[1] = str(numpos1 * 10)
    listanumero[0] = str(numpos1 * 100)

elif len(listanumero) == 4:

    numpos1 = int(listanumero[1])
    numpos2 = int(listanumero[2])
    listanumero[2] = str(numpos2 * 10)
    listanumero[1] = str(numpos2 * 100)
    listanumero[0] = str(nume * 1000)

for numero in listanumero:
    romano += conversor[numero]

print("O numero romano de %s é %s " % (numeroinserido, romano))

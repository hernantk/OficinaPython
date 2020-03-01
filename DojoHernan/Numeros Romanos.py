conversor={"1":"I","2":"II","3":"III",
            "4":"IV","5":"V","6":"VI",
            "7":"VII","8":"VIII","9":"IX",
           "10":"X","20":"XX","30":"XXX",
           "40":"XL","50":"L","60":"LX",
           "70":"LXX","80":"LXXX","90":"XC",
            "100":"C", "200":"CC", "300":"CCC",
            "400":"CD", "500":"D", "600":"DC",
            "700":"DCC", "800":"DCCC", "900":"CM",

            "1000":"M","2000":"MM","3000":"MMM",
            "4000":"MMMM","5000":"_V","6000":"_VI",
            "7000":"_VII","8000":"_VIII","9000":"_IX",
           "0":""
}


numero=input("Insira um numero")
romano=""
dsad = list(numero)
nume=int(dsad[0])
tamanhonumero=int(len(dsad))


if len(dsad)==1:

    print("-")


elif len(dsad)==2:

    dsad[0]=str(nume*10)

elif len(dsad)==3:

    nume1 = int(dsad[1])
    dsad[1]=str(nume1*10)
    dsad[0]=str(nume*100)

elif len(dsad)==4:

    nume1 = int(dsad[1])
    nume2 = int(dsad[2])
    dsad[2]=str(nume2*10)
    dsad[1]=str(nume1*100)
    dsad[0]=str(nume*1000)



for number in dsad:
        romano+=conversor[number]

print("O numero romano de %s é %s "%(numero,romano))




lista = []

for i in range(100):

    numero = i + 1

    if numero % 3 == 0 and numero % 5 == 0:
        lista.append("FizzBuzz")

    elif numero % 3 == 0:
        lista.append("Fizz")

    elif numero % 5 == 0:
        lista.append("Buzz")

    else:
        lista.append(i + 1)

    print(lista[i])

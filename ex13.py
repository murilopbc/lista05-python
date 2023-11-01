n1 = float(input("Digite um número:  "))
n2 = float(input("Digite um outro número: "))
n3 = float(input("Digite um terceiro número: "))

media_ponderada = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10

print(f"A sua média é: ", "{:.2f}".format(media_ponderada))

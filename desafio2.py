capital = float(input("Digite seu capital: "))
taxa_juros = float(input("Informe a taxa de juros: "))
anos = float(input("Informe o tempo em anos: "))
montante_final = capital*(taxa_juros + 1)*anos
print("Meu montante é:", montante_final, "reais")

print("Bem-vindo ao sistema de seleção de candidatos!")
print("Por favor, informe os dados abaixo para cada candidato.")

while True:
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()

    if idade > 18 and sexo == "M":
        print("Candidato selecionado! Código: 1")
    elif idade > 20 and sexo == "F":
        print("Candidato selecionado! Código: 2")
    else:
        print("Candidato não atende aos critérios de seleção.")

    opcao = input("Deseja continuar (S/N)? ").upper()
    if opcao != "S":
        break

print("Obrigado por utilizar o sistema de seleção de candidatos!")

def saudar(nome, periodo="dia"):
    if periodo == "dia":
        print(f"bom dia {nome}")
    elif periodo == "tarde":
        print(f"boa tarde {nome}!")
    elif periodo == "noite":
        print(f"boa noite {nome}!")
    else:
        print("período inválido")

nome= str(input("digite seu nome: "))
periodo= str(input("digite o periodo do dia: "))
saudar(nome,periodo)
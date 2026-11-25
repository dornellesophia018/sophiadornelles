cidades=["fortaleza","maracanau","manaus","sao paulo","tocatins"]
busca = input("digite o nome da cidade que queira buscar: ")
if busca in cidades:
    posicao=cidades.index(busca)
    print(f"a cidade {busca} está cadastrada no índice {posicao}")
else:
    print(f"a cidade {busca}não está cadastrada na lista")
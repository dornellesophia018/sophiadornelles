def adriano(custo, dinheiro):
    if dinheiro>=custo:
        return("compra bem sucedida!")
    else:
        return (f"compra mal sucedida. " ,Falta, "{custo-dinheiro}")
dinheiro=float(input("digite o que você tem: "))
custo=float(input("digite o custo das compras: "))
adriano(custo, dinheiro)

                
def compute_bill(lista):
    stock = {
        "banana": 2,
        "pera":4,
        "morango":0,
        "caqui":12
    }
    prices = {
        "banana": 2,
        "pera": 5,
        "morango": 7.5,
        "caqui": 4
    }
    total =0
    naoComprado = []
    for x in lista:
        preco = prices[x]
        if stock[x]>0:
            total=total +preco
            stock[x]=stock[x] -1
        else:
            naoComprado.append(x)
    return total, naoComprado

lista_de_compras = ["banana", "morango", "caqui"]

print(compute_bill(lista_de_compras))
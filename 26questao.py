

codigos = []

quantidade = int(input("Digite a quantidade de códigos a serem cadastrados: "))

for i in range(quantidade):
    codigo = int(input(f"Digite o código do produto {i + 1}: "))
    codigos.append(codigo)

codigo_buscado = int(input("\nDigite o código que deseja verificar: "))

if codigo_buscado in codigos:
    print(f"O código {codigo_buscado} está presente na lista de produtos.")
else:
    print(f"O código {codigo_buscado} NÃO está presente na lista de produtos.")
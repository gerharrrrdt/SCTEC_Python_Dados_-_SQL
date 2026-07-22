id_venda = int(input("Digite o ID de venda: "))
data = str(input("Digite a data da venda (dd/mm/aaaa): "))
vendedor = str(input("Digite o nome do vendedor: "))
cliente = str(input("Digite o nome do cliente: "))
produto = str(input("Digite o produto vendido: "))
categoria = str(input("Digite a categoria: "))
quantidade = int(input("Digite a quantidade: "))
preco_total = None

while (quantidade > 100):
    print("\nQuantidade não disponível em estoque. Tente novamente!\n")
    quantidade = int(input("Digite a quantidade: "))

preço_unitario = float(input("Digite o preço unitário do produto: "))

metodo_pgto = int(input("Método de pagamento:\n[1] À vista\n[2] A prazo\nEscolha o método de pagamento: "))

if(metodo_pgto == 1):
    preco_total = round(preço_unitario*quantidade*0.95,2)
elif(metodo_pgto == 2):
    preco_total = round(preço_unitario*quantidade*1.05,2)
else:
    print("Método de pagamento inválido, escolha uma das opções disponíveis!")
    metodo_pgto = int(input("Método de pagamento:\n[1] À vista\n[2] A prazo\nEscolha o método de pagamento: "))

print("\n"+20*"="+"EXTRATO DE VENDA"+20*"=")
print(f"ID: ", id_venda)
print(f"Data: ", data)
print(f"Vendedor: ", vendedor)
print(f"Cliente: ", cliente)
print(f"Produto: ", produto)
print(f"Categoria: ", categoria)
print(f"Quantidade: ", quantidade)
print(f"Preço Unitário: ", preço_unitario)
print(f"Preço Total: {preco_total:.2f}")
print("\n"+50*"=")
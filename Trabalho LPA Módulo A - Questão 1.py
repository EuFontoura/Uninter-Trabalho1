print("Bem vindo a loja do Gabriel Fontoura")

valor = int(input("Entre com o valor do produto: "))
quantidade = int(input("Entre com a quantidade do produto: "))
total = valor * quantidade
desconto = 0

if total >= 10000: 
    desconto = 0.11
    totalComDesconto = total - (total * 0.11)
    print(f"Total sem desconto: {total}\nTotal com desconto: {totalComDesconto}")
    
elif total >= 6000: 
    desconto = 0.07
    totalComDesconto = total - (total * 0.07)
    print(f"Total sem desconto: {total}\nTotal com desconto: {totalComDesconto}")
    
elif total >= 2500: 
    desconto = 0.04
    totalComDesconto = total - (total * 0.04)
    print(f"Total sem desconto: {total}\nTotal com desconto: {totalComDesconto}")
    
else: 
    print(f"Total sem desconto: {total}\nTotal com desconto: Infelizmente o valor mínimo para desconto não foi atingido")
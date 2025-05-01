
print("Bem vindo a loja do Gabriel Fontoura")

# entrada do valor do produto e quantidade
valor = int(input("Entre com o valor do produto: "))
quantidade = int(input("Entre com a quantidade do produto: "))


# Calculo do valor total
total = valor * quantidade
desconto = 0
totalComDesconto = total # Total com desconto assume o valor total sem desconto pra caso caia no else

if total >= 10000: 
    desconto = 0.11 # desconto de 11%
    totalComDesconto = total - (total * 0.11)
    
elif total >= 6000: 
    desconto = 0.07 # desconto de 7%
    totalComDesconto = total - (total * 0.07)
    
elif total >= 2500: 
    desconto = 0.04 # desconto de 4%
    totalComDesconto = total - (total * 0.04)
    
else: 
    # Não há desconto para valores abaixo de 2500
    print("Infelizmente o valor mínimo para desconto não foi atingido.")

print(f"O valor SEM desconto: R${total:.2f}")
print(f"O valor COM desconto: R${totalComDesconto:.2f}")
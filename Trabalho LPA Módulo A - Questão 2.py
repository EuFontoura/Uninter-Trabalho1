total_pedido = 0 # variável para armazenar os valores 

print("Bem vindo a loja de gelados do Gabriel Fontoura")
print("-" * 20, "Cardápio", "-" *21 )
print("-" * 51 )
print("---|  Tamanho  |  Cupuaçu (CP)  |  Açaí (AC)   |---") 
print("---|     P     |    R$  9.00    |  R$ 11.00    |---") 
print("---|     M     |    R$ 14.00    |  R$ 16.00    |---") 
print("---|     G     |    R$ 18.00    |  R$ 20.00    |---") 
print("-" * 51 )

while True:

    precos = {
            "cp": {"p": 9.00, "m": 14.00, "g": 18.00},
            "ac": {"p": 11.00, "m": 16.00, "g": 20.00}
        }

    sabor = input("Entre com o sabor desejado (CP/AC): ").lower()
    sabor_pedido = 0

    # Verificando o sabor
    if sabor == "ac":
        sabor_pedido = "Açaí"
        # Tamanho
        tamanho = input("Entre com o tamanho desejado (P/M/G): ").lower()

        if tamanho == "p":
            valor = precos["ac"]["p"]
        elif tamanho == "m":
            valor = precos["ac"]["m"]
        elif tamanho == "g":
            valor = precos["ac"]["g"]
        else:
            print("Tamanho inválido. Tente novamente.\n")
            continue
    elif sabor == "cp":
        sabor_pedido = "Cupuaçu"
        # Tamanho
        tamanho = input("Entre com o tamanho desejado (P/M/G): ").lower()

        if tamanho == "p":
            valor = precos["cp"]["p"]
        elif tamanho == "m":
            valor = precos["cp"]["m"]
        elif tamanho == "g":
            valor = precos["cp"]["g"]
        else:
            print("Tamanho inválido. Tente novamente.\n")
            continue
    else:
        print(f"Sabor inválido. Tente novamente.\n")
        continue

    valor = precos[sabor][tamanho]
    total_pedido += valor

# saída do código
    print(f"Você pediu um {sabor_pedido} tamanho {tamanho.upper()}: R$ {valor:.2f}\n")

    continuar = input("Deseja pedir mais alguma coisa? (S/N): ").strip().lower()
    if continuar != "s":
        print(f"\nO valor total a ser pago: R$ {total_pedido:.2f}")
        break


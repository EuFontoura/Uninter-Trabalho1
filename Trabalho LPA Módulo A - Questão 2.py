total_pedido = 0

print("Bem vindo a loja de gelados do Gabriel Fontoura")

while True:
    print("-" * 20, "Cardápio", "-" *21 )
    print("-" * 51 )
    print("---|  Tamanho  |  Cupuaçu (CP)  |  Açaí (AC)   |---") 
    print("---|     P     |    R$  9.00    |  R$ 11.00    |---") 
    print("---|     M     |    R$ 14.00    |  R$ 16.00    |---") 
    print("---|     G     |    R$ 18.00    |  R$ 20.00    |---") 
    print("-" * 51 )

    precos = {
            "cp": {"p": 9.00, "m": 14.00, "g": 18.00},
            "ac": {"p": 11.00, "m": 16.00, "g": 20.00}
        }

    sabor = input("Entre com o sabor desejado (CP/AC): ").lower()
    sabor_pedido = 0

    if sabor == "AC":
        sabor_pedido = "Açaí"
    else:
        sabor_pedido = "Cupuaçu"
        
    if sabor not in ["cp", "ac"]: 
        print(f"Sabor inválido. Tente novamente.\n")
        continue
            
    tamanho = input("Entre com o tamanho desejado (P/M/G): ").lower()
            
    if tamanho not in ["p", "m", "g"]: 
        print("Tamanho inválido. Tente novamente.")
        continue


    valor = precos[sabor][tamanho]
    total_pedido += valor

    print(f"\nVocê pediu um {sabor_pedido} tamanho {tamanho.upper()}: R$ {valor:.2f}")
    print(f"Total parcial: R$ {total_pedido:.2f}")

    continuar = input("Deseja pedir mais alguma coisa? (S/N): ").strip().lower()
    if continuar != "s":
        print(f"O valor total a ser pago: R$ {total_pedido:.2f}")
        break


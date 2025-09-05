import random

# 1. Gerar arquivo com 200 clientes
with open("clientes.txt", "w") as arquivo:
    for i in range(1, 201):
        nome = f"Cliente{i}"
        saldo = random.randint(500, 5000)   # saldo entre 500 e 5000
        divida = random.randint(100, 6000)  # dívida entre 100 e 6000
        arquivo.write(f"{nome},{saldo},{divida}\n")

print("Arquivo clientes.txt gerado com sucesso!")


# 2. Ler arquivo e atualizar saldos
clientes_atualizados = []

with open("clientes.txt", "r") as arquivo:
    for linha in arquivo:
        nome, saldo, divida = linha.strip().split(",")
        saldo = int(saldo)
        divida = int(divida)

        # Comparar saldo e dívida
        if saldo >= divida:
            saldo -= divida   # paga toda a dívida
            divida = 0
        else:
            divida -= saldo   # reduz a dívida pelo saldo disponível
            saldo = 0

        clientes_atualizados.append((nome, saldo, divida))


# 3. Salvar resultados em outro arquivo
with open("clientes_atualizados.txt", "w") as arquivo:
    arquivo.write("Nome,Saldo Atual,Divida Atual\n")
    for nome, saldo, divida in clientes_atualizados:
        arquivo.write(f"{nome},{saldo},{divida}\n")

    print("Arquivo clientes_atualizados.txt criado com os saldos atualizados!")
    total_devedores = sum(1 for _, _, divida in clientes_atualizados if divida > 0)
    total_dividas = sum(divida for _, _, divida in clientes_atualizados)

    arquivo.write(f"\nTotal de clientes com dívida: {total_devedores}\n")
    arquivo.write(f"Valor total das dívidas: {total_dividas}\n")
    
import empregado

while True:
    
    n = input("Digite o seu nome: ")
    sn = input("Digite o seu sobrenome: ")
    id = int(input("Digite o seu ID: "))

    print("-" * 80)

    t = input("Digite o tipo de empregado (C - Comissionado, P - Produção): ").lower()

    if t == "c":
        sb = float(input("Digite o salário base: "))
        c = float(input("Digite o valor da comissão por venda: "))
        qv = int(input("Digite a quantidade vendida: "))

        ec = empregado.EmpregadoComissionado(n, sn, id, sb, c, qv)

        print()
        print(ec)

    elif t == "p":
        rpp = float(input("Digite a remuneração por peça: "))
        qtd = int(input("Digite a quantidade produzida: "))

        ep = empregado.EmpregadoProducao(n, sn, id, rpp, qtd)

        print()
        print(ep)

    else:
        print("Tipo de empregado inválido!")

    continuar = input("\nDeseja cadastrar outro empregado? (S/N): ").lower()
    if continuar != "s":
        break
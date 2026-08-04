import empregado

n = input("Digite o seu nome: ")
sn = input("Digite o seu sobrenome: ")
id = int(input("Digite o seu ID: "))

e = empregado.Empregado(n, sn, id)

while(True):
    print("---------------------------------------------------------------------------------")
    t = input("Digite o tipo de empregado (C - Comissionado, P - PorProduto): ")
    
    if t == "c":
        sb = float(input("Digite o seu salário base: "))
        c = float(input("Digite a sua comissão: "))
        qv = int(input("Digite a quantidade vendida: "))
    
        ec = empregado.EmpregadoComissionado(n, sn, id, sb, c, qv)
        
        print(ec.__str__())
    
    if t == "p":
        sb = float(input("Digite o seu salário base: "))
        c = float(input("Digite a sua comgfissão: "))
        qv = int(input("Digite a quantidade vendida: "))
        
        ep = empregado.EmpregadoPorProduto(n, sn, id, sb, c, qv)
        
        print(ep.__str__())
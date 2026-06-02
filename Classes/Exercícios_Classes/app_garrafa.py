from garrafa import garrafa

c = int(input("Digite a capacidade da garrafa: "))
g = garrafa(c)
d = str(input("Deseja encher(e) ou despejar(d): "))

print(str(g))

if d == "e":
    q = int(input("Digite a quantidade a ser enchida: "))
    g.encher(q)
    if q > g.capacidade:
        print("A garrafa foi enchida até sua capacidade máxima.")
        
elif d == "d":
    q = int(input("Digite a quantidade a ser despejada: "))
    g.despeja(q)
    if q > g.nivel:
        print("A garrafa foi esvaziada completamente.")

print(str(g))
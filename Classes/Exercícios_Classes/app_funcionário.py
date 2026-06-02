from funcionário import funcionário

n = input("Digite o nome do funcionário: ")
c = int(input("Digite o código do funcionário: "))
s = float(input("Digite o salário do funcionário: "))
f = funcionário(c,n,s)

d = float(input("Digite o percentual de aumento do salário: "))
f.aumentarSalario(d)
print(f)
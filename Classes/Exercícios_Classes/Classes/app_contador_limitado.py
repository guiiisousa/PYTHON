from Classes.Exercícios_Classes.Herança.contador_limitado import ContadorLimitado

li = int(input("Digite o limite inferior do contador: "))
ls = int(input("Digite o limite superior do contador: "))

c = ContadorLimitado(li, ls)

d = input("Deseja consultar, incrementar ou decrementar o contador: ")

match d:
    case "consultar":
        print(f"O valor do contador é: {c.consultar()}")
        
    case "incrementar":
        c.incrementar()
        print(f"O valor do contador é: {c.consultar()}")
        
    case "decrementar":
        c.decrementar()
        print(f"O valor do contador é: {c.consultar()}")
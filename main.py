if __name__ == "__main__":

    p = input("Qual programa você quer usar? (1 - compras) (2 - notas)")

    if p == "1":

        import compras as compras

        carrinho = {}
        i = 1

        while i > 0:  
                
                c = input("Vai comprar? (s/n) ")
                if c == "s":
                    n = input("Digite o nome do produto a ser adicionado: ")
                    compras.adicionar_produto(carrinho, n)

                if c == "n":
                    print("Obrigado por comprar conosco!")
                    break

                r= input("Quer remover algum produto? (s/n) ")
                if r == "s":
                    n = input("Digite o nome do produto a ser removido: ")
                    compras.remover_produto(carrinho, n)

                e = input("Quer exibir o carrinho? (s/n) ")
                if e == "s":
                    compras.exibir_carrinho(carrinho)
                
                v = input("Quer verificar se um produto está no carrinho? (s/n) ")
                if v == "s":
                    n = input("Digite o nome do produto a ser verificado: ")
                    compras.Verificar_produto(carrinho, n)
    if p == "2":

        import alunos as alunos

        notas = {}
        boletim = []
        i = 1

        while i > 0:

            d = input("Deseja acessar o sistema? (s/n) ")

            if d == "s":
              
                a = input("Vai adicionar um aluno? (s/n) ")

                if a == "s":

                    n = input("Digite o nome do aluno: ")
                    p = input("Fez alguma prova? (s/n) ")

                    if p == "s":
                        qp = input("Quantas provas você fez?")

                        for j in range(int(qp)):
                            nota = float(input(f"Digite a nota da prova {j+1}: "))
                            if n not in notas:
                                notas[qp] = []
                        notas[qp].append(nota)
                    
                    if p == "n":
                        print("Aluno adicionado sem notas.")

                    alunos.Adicionar_Aluno(boletim, n, notas)

                    l = input("Quer listar os alunos? (s/n) ")

                    if l == "s":
                        print(input(alunos.Exibir_Boletim(boletim, n)))

                if a == "n":
                    print("Aluno não adicionado.")

            if d == "n":

                print("Obrigado por usar nosso sistema de notas!")
                break
           
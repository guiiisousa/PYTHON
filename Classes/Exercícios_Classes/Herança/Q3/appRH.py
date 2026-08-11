from Funcionario import Funcionario
from Gerente import Gerente
from Desenvolvedor import Desenvolvedor
from Departamento import Departamento


if __name__ == "__main__":

    try:

        d = input("Você deseja criar um departamento? (s/n): ").strip().lower()

        if d == "s":

            n = input("Digite o nome do departamento: ")
            departamento = Departamento(n)

            while True:

                f = input("Você deseja adicionar um funcionário? (s/n): ").strip().lower()

                if f == "s":

                    nf = input("Qual o nome do funcionário? ")
                    sb = float(input("Qual o salário base? "))
                    cf = input(
                        "Qual o cargo do funcionário? (Gerente-G / Desenvolvedor-D / Normal-N): ").strip().lower()

                    if cf == "g":
                        bonus = float(input("Qual o bônus do gerente? "))
                        gerente = Gerente(nf, sb, bonus)
                        departamento.adicionar_funcionario(gerente)
                        print("Gerente adicionado!")

                    elif cf == "d":
                        he = int(input("Quantas horas extras? "))
                        vh = float(input("Qual o valor da hora extra? "))
                        desenvolvedor = Desenvolvedor(nf,sb,he,vh)
                        departamento.adicionar_funcionario(desenvolvedor)
                        print("Desenvolvedor adicionado!")

                    elif cf == "n":
                        funcionario = Funcionario(nf,sb)
                        departamento.adicionar_funcionario(funcionario)
                        print("Funcionário adicionado!")

                    else:
                        print("Cargo inválido.")

                elif f == "n":
                    break

                else:
                    print("Digite apenas 's' ou 'n'.")

            while True:

                df = input("\nDeseja calcular o salário total (S), ver funcionários (V) ou sair (Q)? ").strip().lower()

                if df == "s":
                    print(f"Salário total do departamento "f"{departamento.nome}: "f"R$ {departamento.calcular_salario_total():.2f}")
                elif df == "v":
                    print(departamento)
                elif df == "q":
                    print("Programa encerrado.")
                    break
                else:
                    print("Opção inválida.")

    except ValueError as e:

        print(f"Ocorreu um erro de valor: {e}")
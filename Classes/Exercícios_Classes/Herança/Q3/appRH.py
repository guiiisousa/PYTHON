import Funcionario
import Gerente
import Desenvolvedor
import Departamento

if __name__ == "__main__":
    try:
        d = input("Você deseja criar um departamento? (s/n): ").strip().lower()

        if d == 's':
            n = input("Digite o nome do departamento: ")
            departamento = Departamento.Departamento(n)

            while True:
                f = input("Você deseja adicionar um funcionário? (s/n): ").strip().lower()
                if f == 's':
                    nf = input("Qual o nome do funcionário?")
                    sb = float(input("Qual o salário base?"))
            
                    funcionario = Funcionario(nf,sb)

                    cf = input("Qual o cargo do funcionário? ( Gerente-G / Desenvolvedor-D / Normal-N)").strip().lower()

                    if cf == "g":
                        gerente = Gerente(funcionario)
                        departamento.adicionar_funcionario(gerente)
                    
                    if cf == "d":
                        he = int(input("Quantas horas extras?"))
                        vh = float(input("Qual o valor da hora extra?"))
                        desenvolvedor = Desenvolvedor(he, vh)
                        departamento.adicionar_funcionario(desenvolvedor)

                    if cf == "n":
                        departamento.adicionar_funcionario(funcionario)

                if  f == 'n':
                    df = input("Deseja calcular o salário total do departamento (S), ver todos os funcionários (V) ou sair (Q)?").strip().lower()
                    
                    if df == 's':
                        print(f"Salário total do departamento {departamento.nome}: R$ {departamento.calcular_salario_total():.2f}")
                    if df == 'v':
                        print(f"Funcionários do departamento {departamento.nome}:")
                        for funcionario in departamento.funcionarios:
                            print(f"- {funcionario.nome} (Salário: R$ {funcionario.calcular_salario():.2f})")
                    if df == 'q':
                        break
    except Exception as e:
        if isinstance(e, ValueError):
            print(f"Ocorreu um erro de valor: {e}")
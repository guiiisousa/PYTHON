from Funcionario import Funcionario

class Departamento:
    def __init__(self, nome):
        self._nome = nome
        self.__funcionarios = [] 

    @property
    def nome(self):
        if isinstance(self._nome, str):
            return self._nome
        else:
            raise TypeError("O nome do departamento deve ser uma string.")  

    def adicionar_funcionario(self, funcionario):
        if isinstance(funcionario, Funcionario):
            self.__funcionarios.append(funcionario)
        else:
            raise TypeError("O funcionário deve ser uma instância da classe Funcionario.")

    def calcular_salario_total(self):
        total = 0
        for funcionario in self.__funcionarios:
            total += funcionario.calcular_salario()
        return total

    def __str__(self):
        return f"Nome do Departamento: {self.nome}\nQuantidade de funcionários: {len(self.__funcionarios)}"

    def __repr__(self):
        return f"Departamento(nome={self.nome}, funcionarios={self.__funcionarios})"
    
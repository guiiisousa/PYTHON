class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self._salario_base = salario_base  

    @property
    def calcular_salario(self):
        return self._salario_base

    
    def salario_base(self, valor):
        if valor < 0:
            raise ValueError("O salário base não pode ser negativo.")
        self._salario_base = valor

    def calcular_salario(self):
        return self._salario_base

    def __str__(self):
        return f"Nome:{self.nome}\nSalário Base: R${self._salario_base:.2f}"

    def __repr__(self):
        return f"Funcionario(nome={self.nome}, salario_base={self._salario_base})"
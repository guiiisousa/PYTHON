import Funcionario
import Departamento
import Desenvolvedor

class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus_fixo=1500.0):
        super().__init__(nome, salario_base)  
        self.bonus_fixo = bonus_fixo

    def calcular_salario(self):
        return super().calcular_salario() + self.bonus_fixo


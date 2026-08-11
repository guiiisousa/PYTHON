import Funcionario
import Departamento
import Gerente

class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario_base, horas_extras, valor_hora):
        super().__init__(nome, salario_base)
        if isinstance(horas_extras, int) and horas_extras >= 0:
            self.horas_extras = horas_extras
        if isinstance(valor_hora, (int, float)) and valor_hora >= 0:
            self.valor_hora = valor_hora

    def calcular_salario(self):
        if(self.horas_extras * self.valor_hora) > 0:
            return super().calcular_salario() + (self.horas_extras * self.valor_hora)
        else:
            return f"As horas extras não podem ser negativas. O salário base será retornado: R${super().calcular_salario():.2f}"

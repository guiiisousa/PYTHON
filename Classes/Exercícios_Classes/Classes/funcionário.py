class funcionário:
    def __init__(self,codigo,nome,salario):
        if isinstance(nome,str):
            self._nome = nome
        if isinstance(codigo,int):
            self._codigo = codigo
        if isinstance(salario,(int,float)):
            self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def codigo(self):
        return self._codigo

    @property
    def salario(self):
        return self._salario
    
    @nome.setter
    def nome(self, valor):
        if isinstance(valor,str):
            self._nome = valor
            
    @codigo.setter
    def codigo(self, valor):
        if isinstance(valor,int):
            self._codigo = valor
            
    @salario.setter
    def salario(self, valor):
        if isinstance(valor,(int,float)):
            self._salario = valor

    def aumentarSalario(self, percentual):
        if isinstance(percentual,(int,float)):
            self._salario += self._salario * (percentual/100)

    def __str__(self):
        return f"Nome: {self._nome}\nCódigo: {self._codigo}\nSalário: R$ {self._salario:.2f}"
    

            
class Empregado:
    def __init__(self, nome, sobrenome, numero_id):
        if isinstance(nome, str):
            self._nome = nome
            
        if isinstance(sobrenome, str):
            self._sobrenome = sobrenome
            
        if isinstance(numero_id, int):
            self._numero_id = numero_id
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def sobrenome(self):    
        return self._sobrenome
    
    @property
    def numero_id(self):
        return self._numero_id
    
    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str):
            self._nome = valor
            
    @sobrenome.setter
    def sobrenome(self, valor):
        if isinstance(valor, str):
            self._sobrenome = valor
            
    @numero_id.setter
    def numero_id(self, valor):
        if isinstance(valor, int):
            self._numero_id = valor
    
    def __str__(self):
        return (f'Nome: {self._nome}\nSobrenome: {self._sobrenome}\nNúmero de ID: {self._numero_id}')
    
    def desconto(self, valor : float):
            return valor/100
    def rendimento(self):
            return 
        
class EmpregadoComissionado(Empregado):
    def __init__(self,nome,sobrenome,numero_id,salario_base=0,comissao=0,quantidade_vendida=0):
        super().__init__(nome,sobrenome,numero_id)
        
        self._salario_base = salario_base
        self._comissao = comissao     
        self._quantidade_vendida = quantidade_vendida
            
    @property
    def salario_base(self):
        return self._salario_base
    
    @property
    def comissao(self):
        return self._comissao
    
    @property
    def quantidade_vendida(self):
        return self._quantidade_vendida
    
    def __str__(self):
        base = super().__str__()
        salario_liquido = self._salario_base + self.rendimento()
        desconto = self.desconto(8)
        salario_bruto = salario_liquido - desconto
        
        return f'{base}\nSalario Base: R${self._salario_base:.2f}\nComissao: {self._comissao}\nQuantidade Vendida: {self._quantidade_vendida}\nSalário Líquido: R${salario_liquido:.2f}\nDesconto: R${desconto:.2f}\nSalario Bruto: R${salario_bruto:.2f}'    
    
    def desconto(self, valor : float):
        return self.rendimento() * super().desconto(valor)
    
    def rendimento(self):
        return self._comissao * self._quantidade_vendida
    
class EmpregadoProducao(Empregado):
    def __init__(self, nome, sobrenome, numero_id, remuneracao_por_peca = 0, quantidade = 0):
        super().__init__(nome, sobrenome, numero_id)
        
        if isinstance(remuneracao_por_peca,(float)):
            self._remuneracao_por_peca = remuneracao_por_peca
            
        if isinstance(quantidade,(int)):
            self._quantidade = quantidade
            
    def desconto(self, valor):
        return self._rendimento() * super().desconto(valor)
            
    def rendimento(self, quantidade, remuneracao_por_peca):
        return quantidade * remuneracao_por_peca
        
    def __str__(self):
        base = super().__str__()
        desconto = self.desconto(5)
        salario_liquido = self.rendimento(self._remuneracao_por_peca, self._quantidade)
        salario_bruto = salario_liquido - desconto
        return f'{base}\nRemuneração por peça: {self._remuneracao_por_peca}\n Quantidade de itens: {self._quantidade}\nRendimentos: {salario_liquido}\nDesconto: {desconto}\nSalario Bruto: {salario_bruto}'
        
        
# e = Empregado("João", "Silva", 12345)
# ec = EmpregadoComissionado("Maria", "Souza", 67890, 2000.0, 100.0, 10)

# print(ec.__str__())
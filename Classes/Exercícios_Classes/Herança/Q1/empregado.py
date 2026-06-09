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
    
    def desconto(self, valor):
        if isinstance(valor, (int, float)):
            return valor
        else:
            raise ValueError("Valor deve ser um número inteiro ou float.")
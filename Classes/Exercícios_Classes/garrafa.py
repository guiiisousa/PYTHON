class garrafa:
    def __init__(self,capacidade):
        if isinstance(capacidade,int):
            self._capacidade = capacidade
            self._volume = 0
    
    @property
    def capacidade(self):
        return self._capacidade
    
    @property
    def nivel(self):
        return self._volume
    
    @capacidade.setter
    def capacidade(self, valor):
        if isinstance(valor,int):
            self._capacidade = valor
    
    def encher(self,valor):
        if valor > self._capacidade:
            self._volume = self._capacidade
        else:
            self._volume += valor
    
    def despeja(self,valor):
        if valor > self._volume:
            self._volume = 0
        else:
            self._volume -= valor
            
    def __str__(self):
        return f"Garrafa (capacidade={self._capacidade}, volume={self._volume})"
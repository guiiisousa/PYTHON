class contador_limitado:
    def __init__(self,limite_inferior, limite_superior):
        if isinstance(limite_inferior,int):
            self._limite_inferior = limite_inferior
        if isinstance(limite_superior,int):
            self._limite_superior = limite_superior
        self._contador = limite_inferior
        
    @property
    def contador(self):
        return self._contador
    
    @property
    def limite_inferior(self):
        return self._limite_inferior
    
    @contador.setter
    def contador(self, valor):
        if isinstance(valor,int) and valor > 0:
            self._contador = valor
                
    def contador(self, valor):
        if isinstance(valor,int):
            self._contador = valor
    
    def incrementar(self):
        if self._contador < self._limite_superior:
            self._contador += 1
            
        else:
            self.contador = self._limite_inferior
    
    def decrementar(self):
        if self._contador > self._limite_inferior:
            self._contador -= 1
        else:
            self.contador = self._limite_superior

    def __str__(self):
        return f"Contador: {self._contador}, Limite Inferior: {self._limite_inferior}, Limite Superior: {self._limite_superior}"
    
    
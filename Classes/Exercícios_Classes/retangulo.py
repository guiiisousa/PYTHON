class retangulo:
    
    def __init__(self,base,altura):
        if isinstance(altura,int):
            self._altura = altura       
        if isinstance(base,int):
            self._base = base
        
    @property
    def base(self):
        return self._base    
    
    @base.setter
    def base(self, valor):
        if isinstance(valor,int):
            self._base = valor
    
    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if isinstance(valor,int):
            self._altura = valor

    def areaRetangulo(self):
        return self._altura * self._base
    
    def perimetroRetangulo(self):
        return 2*self._altura + 2*self._base
    
    def diagonalRetangulo(self):
        return ((self._altura**2)+(self._base**2))**0.5
    
    def __repr__(self):
        return f"Retangulo(base={self._base}, altura={self._altura})"
    
    def __str__(self):
        return f"Área: {self.areaRetangulo()}\nPerimetro: {self.perimetroRetangulo()}\nDiagonal: {self.diagonalRetangulo()}"

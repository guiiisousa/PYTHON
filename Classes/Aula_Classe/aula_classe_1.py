class Ponto:
    
    def __init__(self,x=0,y=0):
        
        if isinstance(x,(int)):
            self._xCoord = x    
        
        if isinstance(y,(int)):
            self._yCoord = y    
            
    @property
    def xCoord(self):
        return self._xCoord
    
    @property
    def yCoord(self):
        return self._yCoord
    @property
    def xCoord(self,x):
        self._xCoord = x
           
    @property
    def yCoord(self,y):
        self._yCoord = y

    def distancia(self,other):
        if isinstance(other,Ponto):
            return ((self._xCoord - other._xCoord)**2 + (self._yCoord - other._yCoord)**2)**0.5
        
    def __str__(self):
        return f"({self._xCoord},{self._yCoord})"
    
# p = Ponto(3,4)
# print(p)

# print(f"Distância: {p.distancia(Ponto(0,0)):.2f}")

class ponto3D(Ponto):

    def __init__(self,x=0,y=0,z=0):
        super().__init__(x,y)
        if isinstance(z,(int)):
            self._zCoord = z
                 
    def distancia(self,other):
        if isinstance(other,ponto3D):
            return ((self._xCoord - other._xCoord)**2 + (self._yCoord - other._yCoord)**2 + (self._zCoord - other._zCoord)**2)**0.5
        
p3 = ponto3D(8,6,0)
print(p3)

print(f"Distância: {p3.distancia(ponto3D(0,0,0)):.2f}")
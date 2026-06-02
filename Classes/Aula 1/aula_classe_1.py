class Plano_Cartesiano:
    
    def __init__(self,x=0,y=0):
        
        if isinstance(x,(int,float)):
            self.xCoord = x    
        
        if isinstance(y,(int,float)):
            self.yCoord = y    
            
    @property
    def xCoord(self):
        return self.xCoord
    
    @property
    def yCoord(self):
        return self.yCoord

    @property
    def xCoord(self,x):
        self.xCoord = x
           
    @property
    def yCoord(self,y):
        self.xCoord = y
        
    def _str_(self):
        return f"({self.xCoord},{self.yCoord})"
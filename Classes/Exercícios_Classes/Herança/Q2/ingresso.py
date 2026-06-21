class Ingresso():
    def __init__(self, valor, nomeDoEvento):
        if isinstance(valor, (float, int)):
            self._valor = valor
        self._nomeDoEvento = nomeDoEvento

    @property
    def valor(self):
        return self._valor

    def getTipoIngresso(valor):
        if valor == "IngressoNormal":
            return "Ingresso Normal"
        
        elif valor == "IngressoaVip":
            return "Ingresso Vip"
    
    def toString(self):
        return f"Nome: {self._nomeDoEvento}\nValor: R${self._valor:.2f}"
    
class IngressoVip(Ingresso):
    def __init__ (self, valor, nomeDoEvento, valorAdicional):
        super().__init__(valor,nomeDoEvento)
        if isinstance(valorAdicional, (float)):
            self._valorAdicional = valorAdicional

    def toString(self):
        base = super().toString()
        valorFinal = self._valor + self._valorAdicional
        return f"{base}\n/Valor Adicional: R${self._valorAdicional:.2f}\nValor Final: R${valorFinal:.2f}"
    
    def getTipoIngresso(self):
        return super().getTipoIngresso(IngressoVip)
    
class IngressoNormal(Ingresso):
    def __init__(self, valor, nomeDoEvento):
        super().__init__(valor, nomeDoEvento)

    def toString(self):
        base = super().toString()
        valorFinal = self._valor
        return f"{base}\nValor Final: R${valorFinal:.2f}"
    
    def getTipoIngresso(self):
        return super().getTipoIngresso(IngressoNormal)
    
i = Ingresso(10, "Rock In Rio")
print(i.toString())

iV = IngressoVip(10, "Eu", 67.67)
print(iV.toString())

iN = IngressoNormal(10, "Lollapaloza")
print(iN.toString())
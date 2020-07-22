class  Produto:
    def __init__(self, sku, caf, peso_real, peso_desenho, descricao):
        self._sku = sku 
        self._caf = caf
        self._peso_real = float(peso_real)
        self._peso_desenho = float(peso_desenho)
        self._descricao = descricao
    
    @property
    def passou_do_limite(self):
        if self._peso_desenho*1.05 < self._peso_real:
            return True
        else:
            return False
    @property
    def sobrepeso(self):
        return self._peso_real - self._peso_desenho
    
    @property
    def porcentos_fora(self):
        return self.sobrepeso*100/self.peso_desenho
    
    @property
    def sku(self):
        return self._sku
    
    @property
    def caf(self):
        return self._caf

    @property
    def peso_real(self):
        return self._peso_real

    @property
    def peso_desenho(self):
        return self._peso_desenho
    
    @property
    def peso_real(self):
        return self._peso_real

    @property
    def descricao(self):
        return self._descricao

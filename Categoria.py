
class Categoria:

    def __init__(self,nome:str) -> None:
        self._nome = nome

    
    def getNome(self)->str:
        return self._nome
    
    def setNome(self,nome:str)->None:
        self._nome = nome
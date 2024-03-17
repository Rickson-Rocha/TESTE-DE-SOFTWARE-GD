
from datetime import date

from Categoria import Categoria


class Despesa:

    def __init__(self,categoria:Categoria,valor:float,data:date,nomeDespesa:str) -> None:
        self._categoria = categoria
        self._valor = valor
        self._nomeDespesa = nomeDespesa

    
    def getValor(self)->float:
        return self._valor
    
    def getCategoria(self)->Categoria:
        return self._categoria
    
    def getNomeDespesa(self)->str:
        return self._nomeDespesa

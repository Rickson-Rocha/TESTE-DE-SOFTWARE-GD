
from datetime import date
from typing import List

from Despesa import Categoria


class Despesa:

    def __init__(self,categoria:Categoria,valor:float,data:date,nomeDespesa:str) -> None:
        self._categoria = categoria
        self._valor = valor
        self._nomeDespesa = nomeDespesa

    def obter_valor_despesa(self,valor:float)->None:
        # if valor < 0:
        #      raise ValueError("O valor do item de despesa deve ser positivo")
        # self.valor = valor
        pass
        

    def getValor(self)->float:
        return self._valor
    
    def getCategoria(self)->Categoria:
        return self._categoria
    
    def getNomeDespesa(self)->str:
        return self._nomeDespesa

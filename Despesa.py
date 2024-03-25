from datetime import date

from Categoria import Categoria


class Despesa:

    def __init__(self, categoria: Categoria, valor: float, data: date, nomeDespesa: str) -> None:
        if not nomeDespesa:
            raise ValueError("O nome da despesa não pode ser vazio")
        self._categoria = categoria
        self._valor = valor
        self._nomeDespesa = nomeDespesa
        self._data = data

    def obter_valor_despesa(self, valor: float) -> None:
         if valor < 0 :
             raise ValueError("|Atenção: O valor do item de despesa deve ser positivo|")
         self.valor = valor
    
    def getValor(self) -> float:
        return self._valor
    
    def getCategoria(self) -> Categoria:
        return self._categoria
    
    def getData(self)->date:
        return self._data
    
    def getNomeDespesa(self) -> str:
        return self._nomeDespesa

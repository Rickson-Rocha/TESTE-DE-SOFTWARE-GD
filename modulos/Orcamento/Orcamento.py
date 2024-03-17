from typing import Dict, List

from modulos.Categoria.Categoria import Categoria
from modulos.Despesa import Despesa
from modulos.Despesa.Despesa import Despesa


class Orcamento:

    def __init__(self,orcamentoMensal:float) -> None:
        self._orcamentoMensal = orcamentoMensal
        self.despesas: List[Despesa] = []

    def definirOrcamentoMensal(novoOrcamento:float):
        pass

    def adicionarDespesa(despesa:Despesa):
        pass

    def calcularTotalDespesa(self)->float:
        pass

    def calcularProgressoOrcamento(self)->float:
        pass

    def resumoDespesasPorCategoria(despesas: List[Despesa]) -> Dict[Categoria, float]:
      pass
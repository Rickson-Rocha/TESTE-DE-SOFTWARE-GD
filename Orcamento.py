from typing import Dict, List

from Despesa import Despesa
from Categoria import Categoria


class Orcamento:

    def __init__(self,orcamentoMensal:float) -> None:
        self._orcamentoMensal = orcamentoMensal
        self.despesas: List[Despesa] = []

    def definirOrcamentoMensal(self,novoOrcamento:float):

        if not isinstance(novoOrcamento, (int, float)):
            raise ValueError('O orçamento mensal deve ser numérico.')
        elif novoOrcamento == '':
            raise ValueError('O orçamento mensal não pode ser vazio.')
        elif novoOrcamento < 0:
            raise ValueError('O orçamento não pode ser um valor negativo.')
        elif novoOrcamento == 0:
            raise ValueError('O orçamento mensal deve ser maior que zero.')
        self._orcamentoMensal = novoOrcamento
        
    def adicionarDespesa(self, despesa:Despesa):
        
        total_despesas = self.calcularTotalDespesa()
        if total_despesas + despesa.getValor() > self._orcamentoMensal:
            raise ValueError('A despesa excede o orçamento mensal.')
        self.despesas.append(despesa)

    def removerDespesa(self, despesa: Despesa):
        self.despesas.remove(despesa)

    def calcularTotalDespesa(self)->float:
        total = sum(despesa.getValor() for despesa in self.despesas)
        return total

    def calcularProgressoOrcamento(self) -> str:

        total_gasto = self.calcularTotalDespesa()
        progresso = (total_gasto / self._orcamentoMensal) * 100 if self._orcamentoMensal > 0 else 0
        mensagem_progresso = f"Progresso do orçamento: {progresso:.2f}%"
        return mensagem_progresso

    def resumoDespesasPorCategoria(self, despesas: List[Despesa]) -> Dict[str, float]:

        resumo: Dict[str, float] = {}
        for despesa in despesas:
            categoria = despesa.getCategoria().getNome()
            if categoria in resumo:
                resumo[categoria] += despesa.getValor()
            else:
                resumo[categoria] = despesa.getValor()
        return resumo
    
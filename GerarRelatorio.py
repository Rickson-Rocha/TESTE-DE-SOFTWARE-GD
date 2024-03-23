from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from typing import Dict, List
from datetime import date

from Orcamento import Orcamento
from Despesa import Despesa


class GeradorRelatorios:
    def gerarRelatorioDespesasPorCategoria(self, orcamento: Orcamento) -> str:
        if not orcamento.despesas:
            return "Não há despesas para gerar relatório."

        relatorio = ""
        despesas_por_categoria: Dict[str, List[Despesa]] = {}

        for despesa in orcamento.despesas:
            categoria = despesa.getCategoria().getNome()
            if categoria in despesas_por_categoria:
                despesas_por_categoria[categoria].append(despesa)
            else:
                despesas_por_categoria[categoria] = [despesa]

        for categoria, despesas in despesas_por_categoria.items():
            relatorio += f"Categoria: {categoria}\n"
            total_despesas = sum(despesa.getValor() for despesa in despesas)
            relatorio += f"Total de despesas: R$ {total_despesas:.2f}\n"
            relatorio += "Despesas:\n"
            for despesa in despesas:
                relatorio += f"- Despesa: {despesa.getNomeDespesa()}, Valor: R$ {despesa.getValor():.2f}, Data: {despesa.getData().strftime('%d/%m/%Y')}\n"
            relatorio += "\n"

        return relatorio.strip()

    def exportarRelatorioParaCSV(self, relatorio: str, nome_arquivo: str) -> None:
        with open(nome_arquivo, "w", newline="") as file:
            file.write(relatorio)

    def exportarRelatorioParaPDF(self, relatorio: str, nome_arquivo: str) -> None:


        doc = SimpleDocTemplate(nome_arquivo)
        styles = getSampleStyleSheet()
        conteudo = [Paragraph(relatorio, styles["Normal"])]
        doc.build(conteudo)

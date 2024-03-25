import os
import unittest
from datetime import date

from Categoria import Categoria
from Despesa import Despesa
from GerarRelatorio import GeradorRelatorios
from Orcamento import Orcamento


class TestGeradorRelatorios(unittest.TestCase):
    def setUp(self):
        self.gerador_relatorios = GeradorRelatorios()
        self.categoria = Categoria("Alimentação")
        self.despesa = Despesa(self.categoria, 50.0, date.today(), "Almoço")

    def test_gerar_relatorio_despesas_por_categoria_com_orcamento_vazio(self):
        orcamento = Orcamento(12)
        relatorio = self.gerador_relatorios.gerarRelatorioDespesasPorCategoria(orcamento)
        self.assertEqual(relatorio, "Não há despesas para gerar relatório.")

    def test_gerar_relatorio_despesas_por_categoria_com_uma_despesa(self):
        orcamento = Orcamento(1000)
        orcamento.adicionarDespesa(self.despesa)  
        relatorio = self.gerador_relatorios.gerarRelatorioDespesasPorCategoria(orcamento)
        self.assertIn("Categoria: Alimentação", relatorio)
        self.assertIn("Total de despesas: R$ 50.00", relatorio)  
        self.assertIn("- Despesa: Almoço, Valor: R$ 50.00", relatorio)


    def test_exportar_relatorio_para_csv(self):
        relatorio = "Este é um relatório de despesas"
        nome_arquivo = "relatorio_despesas.csv"
        self.gerador_relatorios.exportarRelatorioParaCSV(relatorio, nome_arquivo)
        self.assertTrue(os.path.exists(nome_arquivo))
        with open(nome_arquivo, "r") as file:
            conteudo = file.read()
            self.assertEqual(conteudo, relatorio)

    def test_exportar_relatorio_para_pdf(self):
        relatorio = "Este é um relatório de despesas"
        nome_arquivo = "relatorio_despesas.pdf"
        self.gerador_relatorios.exportarRelatorioParaPDF(relatorio, nome_arquivo)
        self.assertTrue(os.path.exists(nome_arquivo))
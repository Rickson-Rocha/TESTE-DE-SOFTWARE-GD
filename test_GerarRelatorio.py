import unittest
import os
from datetime import date
from Orcamento import Orcamento
from GerarRelatorio import GeradorRelatorios
from Despesa import Despesa

class TestGeradorRelatorios(unittest.TestCase):
    def setUp(self):
        self.gerador_relatorios = GeradorRelatorios()

    def test_gerar_relatorio_despesas_por_categoria_com_orcamento_vazio(self):
        orcamento = Orcamento(12)
        relatorio = self.gerador_relatorios.gerarRelatorioDespesasPorCategoria(orcamento)
        self.assertEqual(relatorio, "Não há despesas para gerar relatório.")

    # def test_gerar_relatorio_despesas_por_categoria_com_uma_despesa(self):
    #     orcamento = Orcamento(1000)
    #     despesa = Despesa(categoria="Alimentação", valor=100.0, data=date.today(), nomeDespesa="Refeição")
    #     orcamento.adicionarDespesa(despesa)
    #     relatorio = self.gerador_relatorios.gerarRelatorioDespesasPorCategoria(orcamento)
    #     self.assertIn("Categoria: Alimentação", relatorio)
    #     self.assertIn("Total de despesas: R$ 100.00", relatorio)
    #     self.assertIn("- Nome: Refeição, Valor: R$ 100.00", relatorio)

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

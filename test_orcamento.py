import unittest
from Orcamento import Orcamento
from Despesa import Despesa
from Categoria import Categoria
from datetime import date



class TestOrcamento(unittest.TestCase):
    def setUp(self):
        self.orcamento = Orcamento(1000.0)

    def test_defini_orcamento_com_valor_nao_numerico(self):

        with self.assertRaises(ValueError):
            self.orcamento.definirOrcamentoMensal('teste')

    def test_defini_orcamento_vazio(self):

        with self.assertRaises(ValueError):
            self.orcamento.definirOrcamentoMensal('')
    

    def test_defini_orcamento_negativo(self):

        with self.assertRaises(ValueError):
            self.orcamento.definirOrcamentoMensal(-10.0)

    def test_defini_orcamento_com_valor_zero(self):

        with self.assertRaises(ValueError):
            self.orcamento.definirOrcamentoMensal(0.0)
    
    def test_defini_orcamento_mensal(self):

        novo_orcamento = 1500.0
        self.orcamento.definirOrcamentoMensal(novo_orcamento)
        self.assertEqual(self.orcamento._orcamentoMensal, novo_orcamento)
    
    def test_adiciona_depesa(self):

        despesa = Despesa(Categoria('Alimentação'), 200.0, date.today(), 'Almoço')
        self.orcamento.adicionarDespesa(despesa)
        self.assertIn(despesa, self.orcamento.despesas)

    def test_adiciona_varias_despesas(self):

        despesas = [
            Despesa(Categoria('Saúde'), 200.0, date.today(), 'Academia'),
            Despesa(Categoria('Transporte'), 50.0, date.today(), 'Uber'),
            Despesa(Categoria('Lazer'), 100.0, date.today(), 'Cinema')
        ]
        for despesa in despesas:
            self.orcamento.adicionarDespesa(despesa)
        
        for despesa in despesas:
            self.assertIn(despesa, self.orcamento.despesas)

    def test_adiciona_despesa_excedendo_orcamento(self):
        self.orcamento.definirOrcamentoMensal(500.0)
        self.orcamento.adicionarDespesa(Despesa(Categoria('Alimentação'), 200.0, date.today(), 'Almoço'))
        self.orcamento.adicionarDespesa(Despesa(Categoria('Transporte'), 300.0, date.today(), 'Ônibus'))
        self.orcamento.adicionarDespesa(Despesa(Categoria('Transporte'), 300.0, date.today(), 'Ônibus'))
        self.orcamento.adicionarDespesa(Despesa(Categoria('Transporte'), 300.0, date.today(), 'Ônibus'))
        self.orcamento.adicionarDespesa(Despesa(Categoria('Transporte'), 300.0, date.today(), 'Ônibus'))
        self.orcamento.adicionarDespesa(Despesa(Categoria('Transporte'), 300.0, date.today(), 'Ônibus'))

        # Adicionar uma nova despesa que excede o orçamento restante
        with self.assertRaises(ValueError):
            self.orcamento.adicionarDespesa(Despesa(Categoria('Lazer'), 1000.0, date.today(), 'Viagem'))


    
    def test_calcula_total_despesas(self):

        self.orcamento.adicionarDespesa(Despesa(Categoria('Alimentação'), 150.0, date.today(), 'Supermercado'))
        self.orcamento.adicionarDespesa(Despesa(Categoria('Transporte'), 50.0, date.today(), 'Gasolina'))
        self.orcamento.adicionarDespesa(Despesa(Categoria('Lazer'), 100.0, date.today(), 'Cinema'))

        total_esperado = 150.0 + 50.0 + 100.0

        total_calculado = self.orcamento.calcularTotalDespesa()
        self.assertEqual(total_calculado, total_esperado)
       
    def test_calcula_total_sem_despesas(self):

        total_calculado = self.orcamento.calcularTotalDespesa()
        self.assertEqual(total_calculado, 0.0)

    def test_calcula_total_com_remocao_despesa(self):

        despesa1 = Despesa(Categoria('Alimentação'), 150.0, date.today(), 'Supermercado')
        despesa2 = Despesa(Categoria('Transporte'), 50.0, date.today(), 'Gasolina')
        self.orcamento.adicionarDespesa(despesa1)
        self.orcamento.adicionarDespesa(despesa2)

        total_esperado = 150.0 + 50.0

        total_calculado = self.orcamento.calcularTotalDespesa()
        self.assertEqual(total_calculado, total_esperado)

        self.orcamento.removerDespesa(despesa1)
        novo_total_esperado = 50.0

        novo_total_calculado = self.orcamento.calcularTotalDespesa()
        self.assertEqual(novo_total_calculado, novo_total_esperado)

    def test_calcula_progresso_orcamento_sem_despesas(self):

        progresso_esperado = "Progresso do orçamento: 0.00%"
        progresso_calculado = self.orcamento.calcularProgressoOrcamento()
        self.assertEqual(progresso_calculado, progresso_esperado)

    def test_calcula_progresso_orcamento_com_despesas(self):

        self.orcamento.adicionarDespesa(Despesa(Categoria('Alimentação'), 500.0, date.today(), 'Supermercado'))
        self.orcamento.adicionarDespesa(Despesa(Categoria('Transporte'), 250.0, date.today(), 'Gasolina'))
        self.orcamento.adicionarDespesa(Despesa(Categoria('Lazer'), 100.0, date.today(), 'Cinema'))
        progresso_esperado = "Progresso do orçamento: 85.00%"
        progresso_calculado = self.orcamento.calcularProgressoOrcamento()
        self.assertEqual(progresso_calculado, progresso_esperado)

    def test_resumo_despesas_por_categoria_sem_despesas(self):

        despesas = []
        resumo_esperado = {}
        resumo_calculado = self.orcamento.resumoDespesasPorCategoria(despesas)
        self.assertEqual(resumo_calculado, resumo_esperado)


    def test_resumo_despesas_por_categoria_com_despesas(self):
        with self.assertRaises(ValueError):
            self.orcamento.adicionarDespesa(Despesa(Categoria('Transporte'), 1900.0, date.today(), 'Ônibus'))

   

if __name__ == '__main__':
    unittest.main()





    
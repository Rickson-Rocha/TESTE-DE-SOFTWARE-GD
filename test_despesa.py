import unittest
from datetime import date

from Categoria import Categoria
from Despesa import Despesa


class TestDespesaMetodos(unittest.TestCase):

    def setUp(self):
        self.categoria = Categoria("Alimentação")
        self.despesa = Despesa(self.categoria, 50.0, date.today(), "Almoço")

    def test_obter_valor_despesa(self):
        novo_valor = 50
        self.despesa.obter_valor_despesa(novo_valor)
        self.assertEqual(self.despesa.getValor(), novo_valor)

    def test_getCategoria(self):
        self.assertEqual(self.despesa.getCategoria(), self.categoria)

    def test_getNomeDespesa(self):
        self.assertEqual(self.despesa.getNomeDespesa(), "Almoço")

    def test_nome_despesa_vazio(self):
        with self.assertRaises(ValueError):
            despesa_vazia = Despesa(self.categoria, 50.0, date.today(), "")
            
    def test_obter_valor_despesa_negativo(self):
        with self.assertRaises(ValueError):
            self.despesa.obter_valor_despesa(-50.0)

if __name__ == '__main__':
    unittest.main()

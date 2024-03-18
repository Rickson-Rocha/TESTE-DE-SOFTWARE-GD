
import unittest
from datetime import date

from Categorias.Categoria import Categoria
from Despesas.Despesa import Despesa


class TestsDespesaMetodos(unittest.TestCase):

    def setUp(self) -> None:
        self.categoria = Categoria("Alimento")
    
    def test_verificar_valor_item_despesa_positivo(self):
        categoria = Categoria("Alimentação")
        despesa = Despesa(categoria,50.0,date.today(),"almoço")
        despesa.obter_valor_despesa(50.0)
        self.assertEquals(despesa.getValor(),50.0)

if __name__ == '__main__':
    unittest.main()

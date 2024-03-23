import unittest

from Categoria import Categoria


class TestCategoria(unittest.TestCase):

    def test_criar_categoria(self):
        with self.assertRaises(ValueError):
            categoria = Categoria("")
            

    def test_criar_categoria_numero(self):
        with self.assertRaises(ValueError):
            categoria = Categoria("123")


    def test_editar_categoria(self):
        categoria = Categoria("Categoria Teste")

        with self.assertRaises(ValueError):
            categoria.setNome("")

        categoria.setNome("Nova Categoria")
        self.assertEqual(categoria.getNome(), "Nova Categoria")


    def test_editar_categoria_numero(self):
        categoria = Categoria("Categoria Teste")

        with self.assertRaises(ValueError):
            categoria.setNome("123")

        self.assertEqual(categoria.getNome(), "Categoria Teste")

    def test_obter_categoria(self):
        categoria = Categoria("Categoria Teste")
        nome_categoria = categoria.getNome()
        self.assertEqual(nome_categoria, "Categoria Teste")

if __name__ == '__main__':
    unittest.main()

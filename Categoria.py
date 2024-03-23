import re


class Categoria:

    def __init__(self, nome: str) -> None:
        if nome is None or nome.strip() == "" or re.match(r'^\d+$', nome):
            raise ValueError("O nome da categoria não pode ser vazio ou consistir apenas de números.")
        self._nome = nome

    def getNome(self) -> str:
        return self._nome

    def setNome(self, nome: str) -> None:
        if nome is None or nome.strip() == "" or re.match(r'^\d+$', nome):
            raise ValueError("O nome da categoria não pode ser vazio ou consistir apenas de números.")
        self._nome = nome

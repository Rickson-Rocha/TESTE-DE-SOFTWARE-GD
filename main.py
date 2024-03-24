from datetime import date

from Categoria import Categoria
from Despesa import Despesa
from Orcamento import Orcamento

categoria_alimentacao = Categoria("Alimentação")
categoria_transporte = Categoria("Transporte")
categoria_moradia = Categoria("Moradia")


orcamento = Orcamento(3000)

despesa1 = Despesa(categoria_alimentacao, 500, date(2024, 3, 15), "Compras no supermercado")
despesa2 = Despesa(categoria_transporte, 200, date(2024, 3, 10), "Combustível")
despesa3 = Despesa(categoria_moradia, 1500, date(2024, 3, 5), "Aluguel")



orcamento.adicionarDespesa(despesa1)
orcamento.adicionarDespesa(despesa2)
orcamento.adicionarDespesa(despesa3)
print(orcamento.calcularTotalDespesa())

print(f'Esse é o valor original da despesa: ${orcamento.calcularProgressoOrcamento()}')


orcamento.removerDespesa(despesa2)
print(orcamento.calcularTotalDespesa())
print(f'Esse é o valor original da despesa após remover a despesa2: ${orcamento.calcularProgressoOrcamento()}')

print(orcamento.calcularProgressoOrcamento())

resumo_despesas = orcamento.resumoDespesasPorCategoria(orcamento.despesas)
for categoria, total in resumo_despesas.items():
    print(f"Categoria: {categoria} - Total: R${total:.2f}")

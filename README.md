# Introdução

O presente projeto tem como objetivo desenvolver um aplicativo de gerenciamento de despesas que auxilie os usuários a ter um melhor controle sobre suas finanças pessoais, possibilitando que tomem decisões financeiras mais conscientes e eficazes.

A proposta é oferecer uma ferramenta simples e intuitiva que permita registrar e categorizar as despesas diárias, além de fornecer relatórios detalhados para acompanhar o fluxo de caixa e identificar áreas de economia.

O aplicativo fornece as ferramentas necessárias para registrar, categorizar e analisar os gastos, o que permite aos usuários tomar decisões mais conscientes sobre como administrar seu dinheiro.

## Funcionalidades

O aplicativo oferecerá as seguintes funcionalidades:

* **Registro de Despesas:**

* Permite adicionar novas despesas, incluindo a categoria, o valor e a data da despesa.
* Essa funcionalidade é essencial para ter um registro completo dos gastos e poder acompanhá-los ao longo do tempo.

* **Categorização de Despesas:**

* Permite categorizar as despesas em categorias pré-definidas, como alimentação, transporte e moradia.
* Essa funcionalidade facilita a análise dos gastos e a identificação de áreas em que se pode economizar.

* **Resumo de Despesas:**

* Permite visualizar um resumo das despesas por categoria, data – ou período - e valor.
* Essa funcionalidade oferece uma visão geral dos gastos e ajuda a identificar padrões de consumo.

* **Orçamento Mensal:**

* Permite definir um orçamento por período e acompanhar o progresso de gastos em relação ao orçamento definido.
* Importante no controle de gastos e evitar endividamento.

* **Exportação de Dados:**

* Com esta funcionalidade é possível exportar os dados de despesas para um arquivo CSV ou PDF.
* Dessa forma, os dados podem ser usados em outros programas, como planilhas eletrônicas, para análises mais complexas.

## Testes de Unidade

O intuito é testar unidades individuais de código, como funções, métodos ou classes, para garantir que cada unidade de código funcione como esperado, independentemente de outras partes do sistema.

Esse processo deve ser feito de forma automatizada e será executada frequentemente como parte do processo de desenvolvimento para facilitar a detecção precoce de erros e o isolamento de problemas. Essas ações endossam maior confiabilidade do código.

Para o sistema de gerenciamento de despesas serão efetuados os seguintes testes:

* **Testes de Unidade:**

* **Classe Despesa:**

  * **Criar Despesa:**

* Verificar se a despesa é criada com sucesso com os dados informados.
* Verificar se a categoria da despesa é definida corretamente.
* Verificar se o valor da despesa é definido corretamente.
* Verificar se a data da despesa é definida corretamente.


## Testes de Unidade

### Classe Despesa:

#### Editar Despesa:

* Verificar se a despesa é editada com sucesso com os novos dados.
* Verificar se a categoria da despesa é atualizada corretamente.
* Verificar se o valor da despesa é atualizado corretamente.
* Verificar se a data da despesa é atualizada corretamente.

#### Obter Despesa:

* Verificar se a despesa é recuperada com sucesso pelo ID.
* Verificar se todos os dados da despesa são recuperados corretamente.

### Classe Categoria:

#### Criar Categoria:

* Verificar se a categoria é criada com sucesso com o nome informado.

#### Editar Categoria:

* Verificar se a categoria é editada com sucesso com o novo nome.

#### Obter Categoria:

* Verificar se a categoria é recuperada com sucesso pelo ID.
* Verificar se o nome da categoria é recuperado corretamente.

### Classe RelatorioService:

#### Emitir Relatório de Despesas por Categoria:

* Verificar se o relatório é gerado com sucesso com os dados das despesas por categoria.
* Verificar se o formato do relatório está correto.
* Verificar se os dados do relatório estão corretos.

#### Emitir Relatório de Despesas por Data:

* Verificar se o relatório é gerado com sucesso com os dados das despesas por data.
* Verificar se o formato do relatório está correto.
* Verificar se os dados do relatório estão corretos.

### Classe Orcamento:

#### Criar Orcamento:

* Verificar se o orçamento é criado com sucesso com o valor e o mês/ano informados.

#### Editar Orcamento:

* Verificar se o orçamento é editado com sucesso com o novo valor ou mês/ano.

#### Obter Orcamento:

* Verificar se o orçamento é recuperado com sucesso pelo ID.
* Verificar se o valor e o mês/ano do orçamento são recuperados corretamente.

## TECNOLOGIAS

* **Linguagem de programação:** Python
* **Framework:**
* **Banco de dados:** 
* **Biblioteca de testes:** 

## Conclusões

**Observações:**

* A principal conclusão do seu projeto deve ser inserida no espaço em branco.
* As dificuldades encontradas no desenvolvimento do projeto devem ser descritas com mais detalhes.
* A seção de aprendizados pode ser expandida para detalhar outras lições aprendidas durante o processo de desenvolvimento.

**Exemplo de conclusão:**

Como principal conclusão, observou – se que [inserir aqui ]. No desenvolvimento do projeto foram encontradas algumas dificuldades na realização como:  

 sei que lá 

 sei que lá 

 sei que lá 

 

Este trabalho apresentou o TDD e sua importância. A implementação de um processo de testes, mesmo que básico, demonstra ser uma estratégia valiosa para mitigar riscos e otimizar o tempo dedicado à correção de falhas. A filosofia TDD se destaca por garantir que o código seja criado já com testes, permitindo a detecção precoce de erros. Essa abordagem minimiza a necessidade de refatoração extensiva de código escrito há algum tempo, além de promover a padronização e qualidade do código como um todo.  

Entre os aprendizados com o processo de desenvolvimento também foi possível compreender a importância do planejamento, uma vez que um plano de desenvolvimento bem definido, com requisitos claros e objetivos específicos, é fundamental para o sucesso do projeto. 

**Exemplo de descrição de dificuldades:**

* Dificuldade em definir os critérios de aceite para os testes de unidade.
* Dificuldade em lidar com exceções e erros inesperados durante a execução dos testes.
* Dificuldade em manter os testes atualizados com as modificações no código.

    *FALTA * 

Estrutura básica dos testes, incluindo testes que falham devido à falta de implementação. 

Código fonte completo do projeto, incluindo implementação e testes. 
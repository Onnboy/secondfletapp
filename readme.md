### Explicação das Seções

- **Funcionalidades**: Descreve as principais funcionalidades do aplicativo.
- **Configuração do Ambiente Virtual**: Guia o usuário para configurar o ambiente virtual e instalar dependências.
- **Como Executar o Projeto**: Mostra o comando para rodar o aplicativo.
- **Dependências**: Explica brevemente as dependências (mais detalhes no `requirements.txt`).
- **Exemplo de Uso**: Explica como usar o aplicativo, passo a passo.

Esse `README.md` fornece uma documentação clara para usuários e colaboradores entenderem e configurarem o projeto.

# Lista de Tarefas com Flet:
Este é um aplicativo de lista de tarefas simples criado usando o [Flet](https://flet.dev/). Ele permite que os usuários adicionem, removam, marquem tarefas como concluídas e pesquisem por tarefas específicas.

## Funcionalidades:
- Adicionar novas tarefas
- Marcar tarefas como concluídas
- Remover tarefas
- Confirmação de exclusão com diálogo
- Contador de tarefas pendentes
- Busca por tarefas
- Edição de tarefas com duplo clique

## Pré-requisitos:
- Python 3.7 ou superior

## Configuração do Ambiente Virtual:
É recomendável configurar um ambiente virtual para o projeto para gerenciar as dependências de forma isolada.

### Passo a Passo:

1. Clone o repositório do projeto:
    ```bash
    git clone 
    cd nome_do_repositorio

2. Crie um ambiente virtual:
    python3 -m venv .venv // Exemplo!

3. Ative o ambiente virtual:
    - No linux/Mac:
    .venv/Scripts/activate
    - No Windows:
    source .venv/bin/activate

4. Instale as dependências listadas no arquivo requirements.txt:
    pip install -r requirements.txt

# Como Executar o Projeto
    Com o ambiente virtual ativado e as dependências instaladas, execute o aplicativo com:
        python lista_tarefas.py
        Isso abrirá o aplicativo de lista de tarefas com a interface construída em Flet.

# Estrutura do Projeto
    lista_tarefas.py: Código principal do aplicativo de lista de tarefas
    requirements.txt: Lista de dependências do Python necessárias para executar o projeto

# Dependência
    O projeto utiliza várias bibliotecas, incluindo:
        flet: Framework para construção da interface gráfica
        fastapi: Suporte para funcionalidades relacionadas a API (caso seja necessário)
    >Outras dependências úteis para funcionalidades adicionais (detalhes no no requirements.txt).

# Exemplo de Uso
1. Insira uma nova tarefa no campo de texto e clique em "Acrescentar".
2. Marque uma tarefa como concluída clicando na caixa de seleção ao lado dela.
3. Remova uma tarefa clicando no ícone de lixeira, que exibirá uma confirmação.
4. Use a barra de busca para encontrar uma tarefa específica pelo nome.
5. Edite uma tarefa dando um duplo clique sobre o texto dela.

# Contribuição
    Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias no projeto.
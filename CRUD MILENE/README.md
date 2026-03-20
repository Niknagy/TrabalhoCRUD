# Sistema CRUD de Tarefas

## Objetivo

Desenvolver um sistema CRUD em Python com persistência de dados utilizando SQLite para controle de tarefas de limpeza ou manutenção.

## Tecnologias Utilizadas

- Python 3
- SQLite 3

## Estrutura do Projeto

- `db_setup.py`: Script para criação do banco de dados e tabela.
- `crud.py`: Funções para operações CRUD (Create, Read, Update, Delete) e busca.
- `main.py`: Código principal com menu interativo no terminal.
- `gui.py`: Interface gráfica com Tkinter para operações CRUD.
- `app.py`: Aplicação web com Flask e templates HTML.
- `templates/`: Pasta com templates HTML para a versão web.
- `sample_data.py`: Script opcional para inserir tarefas de exemplo.
- `list_tasks.py`: Script para listar todas as tarefas.
- `README.md`: Este arquivo com documentação.

## Instruções de Execução

1. Certifique-se de ter Python 3 instalado.
2. Execute o script de criação do banco: `python db_setup.py` (ou caminho completo)
3. Para versão terminal: `python main.py`
4. Para versão gráfica: `python gui.py`
5. Para versão web: `python app.py` (instale Flask com `pip install flask` se necessário)

## Exemplo de Uso

### Terminal
Ao executar `main.py`, você verá um menu como:

```
Sistema CRUD de Tarefas
1. Inserir tarefa
2. Listar tarefas
3. Atualizar tarefa
4. Excluir tarefa
5. Buscar tarefas
6. Sair
Escolha uma opção:
```

- Escolha 1 para inserir uma nova tarefa, fornecendo os campos solicitados.
- Escolha 2 para listar todas as tarefas.
- Escolha 3 para atualizar uma tarefa existente pelo ID.
- Escolha 4 para excluir uma tarefa pelo ID.
- Escolha 5 para buscar tarefas por nome da tarefa ou funcionário.

### Interface Gráfica
Execute `gui.py` para abrir a interface com botões para cada operação:
- **Inserir Tarefa**: Preencha os campos e clique em "Inserir".
- **Consultar Tarefas**: Visualize todas as tarefas em uma janela de texto.
- **Atualizar Tarefa**: Insira o ID e os novos valores, clique em "Atualizar".
- **Excluir Tarefa**: Insira o ID e clique em "Excluir".

### Versão Web
Execute `app.py` e acesse http://localhost:5000 no navegador:
- **Página Inicial**: Menu com links para operações.
- **Inserir Tarefa**: Formulário HTML para adicionar nova tarefa.
- **Consultar Tarefas**: Tabela com todas as tarefas e links para atualizar/excluir.
- **Atualizar Tarefa**: Formulário pré-preenchido para editar.
- **Excluir Tarefa**: Página de confirmação para deletar.

## Campos da Tarefa

- Funcionário
- Função
- Local
- Tarefa
- Prioridade
- Status
- Data de início (formato YYYY-MM-DD)
- Data de término (formato YYYY-MM-DD)
- Responsável pelo registro
- Data de criação (automática)

## Diferenciais Implementados

- Busca por nome (tarefa ou funcionário)
- Menu interativo no terminal
- Separação de funções CRUD em arquivo separado
- Interface gráfica com Tkinter (telas separadas para cada operação)
- Versão web com Flask e templates HTML responsivos
# CRUD de Fretes (Flask + SQLite)

Projeto de faculdade com sistema CRUD web para cadastro de fretes.

## Tecnologias

- Python 3
- Flask
- SQLite (via modulo nativo `sqlite3`)

## Telas implementadas

- Tela principal
- Tela para consultar dados
- Tela para inserir dados
- Tela para excluir dados
- Tela para atualizar dados

## Estrutura

- `app.py`: aplicacao Flask e rotas das telas
- `database.py`: acesso ao banco e operacoes CRUD
- `schema.sql`: script de criacao da tabela
- `templates/`: paginas HTML
- `static/styles.css`: estilos da interface
- `requirements.txt`: dependencias Python

## Como executar localmente

1. Abra o terminal na pasta do projeto.
2. Instale as dependencias:

```bash
py -m pip install -r requirements.txt
```

3. Rode a aplicacao:

```bash
py app.py
```

4. Abra no navegador:

```text
http://127.0.0.1:5000
```

## Como executar no GitHub Codespaces

1. Abra o repositorio no Codespaces.
2. No terminal do Codespace, rode:

```bash
python -m pip install -r requirements.txt
python app.py
```

3. Quando a porta `5000` aparecer, clique em `Open in Browser`.

Observacao: o `app.py` ja esta configurado para rodar em container (`0.0.0.0` e porta por variavel de ambiente).

## Rodar no Codespaces sem navegador (terminal)

Se voce quiser somente o sisteminha em terminal, rode direto:

```bash
python app_terminal.py
```

Esse modo nao usa Flask e nao precisa abrir porta.

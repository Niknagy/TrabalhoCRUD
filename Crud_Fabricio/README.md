# 🚚 Sistema CRUD de Gerenciamento de Fretes

Uma aplicação web moderna e profissional para gestão completa de fretes, desenvolvida com **Flask** e **SQLite**.

## ✨ Recursos Principais

- ✅ **Interface Intuitiva**: Design moderno com HTML5 semântico e CSS profissional
- 📋 **Consultar**: Visualize todos os fretes cadastrados em uma tabela elegante
- ➕ **Inserir**: Cadastre novos fretes com validação de dados
- ✏️ **Atualizar**: Modifique informações de fretes existentes
- 🗑️ **Excluir**: Remova fretes com confirmação de segurança
- 📱 **Responsivo**: Interface adaptada para desktop, tablet e mobile
- 🎨 **Tema Profissional**: Cores harmoniosas e elementos visuais modernos

## 🛠️ Tecnologias

| Tecnologia | Versão | Propósito |
|-----------|--------|----------|
| Python | 3.x | Linguagem principal |
| Flask | 2.x | Framework web |
| SQLite | Nativo | Banco de dados |
| HTML5 | - | Marcação semântica |
| CSS3 | - | Estilização moderna |

## 📁 Estrutura do Projeto

```
Crud_Fabricio/
├── app.py                 # Aplicação Flask e rotas
├── app_terminal.py        # Interface alternativa (terminal)
├── database.py            # Operações CRUD e banco de dados
├── schema.sql             # Script de criação da tabela
├── requirements.txt       # Dependências Python
├── README.md              # Este arquivo
│
├── static/
│   └── styles.css         # Estilos CSS profissionais
│
└── templates/
	├── base.html          # Template base com header e footer
	├── index.html         # Página principal
	├── consultar.html     # Consulta de fretes
	├── inserir.html       # Cadastro de novo frete
	├── atualizar.html     # Edição de frete
	└── excluir.html       # Remoção de frete
```

## 🚀 Como Executar Localmente

### Pré-requisitos
- Python 3.7+
- pip (gerenciador de pacotes Python)

### Passos
```bash
1. **Navegue até a pasta do projeto:**
```bash
cd path/to/Crud_Fabricio
```
py -m pip install -r requirements.txt
2. **Instale as dependências:**
```

pip install -r requirements.txt

```bash
3. **Inicie a aplicação:**
```

python app.py

```text
4. **Acesse no navegador:**
```

## Como executar no GitHub Codespaces

1. Abra o repositorio no Codespaces.
## 📋 Funcionalidades Detalhadas

### 🏠 Página Principal
- Visão geral do sistema
- Atalhos rápidos para as principais operações
- Indicadores visuais das funcionalidades

### 📊 Consultar Fretes
- Tabela com todos os fretes cadastrados
- Exibição completa de informações (caminhão, motorista, rota, valor, status)
- Status com badges coloridas
- Mensagem quando nenhum frete está cadastrado

### ➕ Inserir Novo Frete
- Formulário intuitivo com campos bem organizados
- Validação de dados em tempo de envio
- Suporte a múltiplos formatos de valor (1500 ou 1500.00)
- Feedback visual de sucesso

### ✏️ Atualizar Frete
- Busca de frete por ID
- Edição de todos os campos
- Seletor de status com opções pré-definidas
- Confirmação visual do frete encontrado

### 🗑️ Excluir Frete  
- Busca segura antes da exclusão
- Preview completo dos dados antes de confirmar
- Alerta visual em vermelho para reforçar ação destrutiva
- Botões de confirmação e cancelamento

## 🎨 Design e UX

### Paleta de Cores
- **Primária**: Azul profissional (#2563eb)
- **Sucesso**: Verde (#10b981)
- **Alerta**: Âmbar (#f59e0b)
- **Erro**: Vermelho (#ef4444)
- **Background**: Tons neutros de cinza

### Recursos de UX
- 🎯 Ícones emoji para rápida identificação
- 🌐 Navegação sticky (fixa) no topo
- ✨ Animações suaves em hover
- 📱 Design mobile-first responsivo
- ♿ HTML semântico para melhor acessibilidade

## 📊 Campos do Frete

| Campo | Tipo | Obrigatoriedade | Exemplo |
|-------|------|-----------------|---------|
| Caminhão | Texto | Obrigatório | Volvo FH 16 |
| Motorista | Texto | Obrigatório | João Silva |
| Origem | Texto | Obrigatório | São Paulo - SP |
| Destino | Texto | Obrigatório | Rio de Janeiro - RJ |
| Carga | Texto | Obrigatório | 2500 kg de mercadoria |
| Valor (R$) | Decimal | Obrigatório | 1500.00 |
| Status | Seleção | Obrigatório | Ativo, Pendente, Entregue, Cancelado |
| Data de Entrega | Data | Obrigatório | 2026-03-24 |

## 💻 Rotas da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Página principal |
| GET | `/consultar` | Lista todos os fretes |
| GET/POST | `/inserir` | Formulário e cadastro de frete |
| GET/POST | `/atualizar` | Busca e edição de frete |
| GET/POST | `/excluir` | Busca e exclusão de frete |

## 🐛 Tratamento de Erros

A aplicação valida:
- ✓ Campos vazios
- ✓ Valores numéricos inválidos
- ✓ IDs inexistentes
- ✓ Datas em formato correto
- ✓ Confirmação antes de operações destrutivas

## 📝 Exemplos de Uso

### Inserir um Frete
1. Clique em **➕ Inserir Dados**
2. Preencha todos os campos
3. Clique em **✅ Salvar Frete**

### Atualizar um Frete  
1. Clique em **✏️ Atualizar Dados**
2. Digite o ID do frete
3. Clique em **🔎 Buscar**
4. Modifique os campos desejados
5. Clique em **✅ Salvar Alterações**

### Excluir um Frete
1. Clique em **🗑️ Excluir Dados**  
2. Digite o ID do frete
3. Clique em **🔎 Buscar**
4. Revise os dados
5. Clique em **❌ Confirmar Exclusão**

## 🔒 Segurança

- Valores são escapados automaticamente pelo Flask/Jinja2
- Validação de entrada antes do processamento
- Confirmações obrigatórias para operações críticas
- Sem exposição de erros internos para o usuário

## 📱 Responsividade

A interface se adapta perfeitamente a:
- 💻 Desktop (1920px+)
- 📊 Tablet (768px - 1024px)
- 📱 Mobile (até 480px)

## 🚢 Deployment

A aplicação pode ser facilmente deployada em plataformas como:
- GitHub Codespaces
- Heroku
- AWS
- PythonAnywhere
- Qualquer servidor com Python

Para deployment, configure a variável de ambiente `PORT`:
```bash
export PORT=8000 && python app.py
```

## 📞 Suporte e Contribuição

Este é um projeto educacional. Para melhorias ou sugestões, abra uma issue.

## 📄 Licença

Projeto acadêmico desenvolvido para fins educacionais.

---

**Desenvolvido com ❤️ em Python + Flask**
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

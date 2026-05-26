# Finanças Start — Refatorado

Projeto reestruturado em Flask com arquitetura MVC, API REST, PostgreSQL e front-end moderno responsivo.

## Principais recursos
- Cadastro e login
- Perfil do usuário
- Dashboard financeiro
- Controle de transações
- Metas financeiras
- Conteúdos de educação financeira

## Estrutura
- `app/models`: modelos do banco
- `app/controllers`: regras e respostas da API
- `app/routes`: blueprints
- `app/services`: lógica de negócio
- `app/templates`: views HTML
- `app/static`: CSS e JS

## Como executar

### 1. Criar ambiente virtual
```bash
python -m venv venv
```

### 2. Ativar
Windows:
```bash
venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar `.env`
Copie `.env.example` para `.env` e ajuste `DATABASE_URL`.

### 5. Rodar o projeto
```bash
python app.py
```

## Banco PostgreSQL
Você pode usar o script `postgres_setup.sql` para criar o banco e a estrutura inicial.

## Observação
Se o PostgreSQL não estiver disponível, o projeto pode usar SQLite em modo local para testes.

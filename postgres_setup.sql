-- Banco de dados para o projeto Finanças Start
-- Ajuste o nome do banco e execute no PostgreSQL.

CREATE DATABASE financas_start;

\c financas_start

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    senha_hash VARCHAR(255) NOT NULL,
    avatar VARCHAR(255),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS transactions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    tipo VARCHAR(20) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    valor NUMERIC(10,2) NOT NULL,
    descricao VARCHAR(255),
    data DATE NOT NULL DEFAULT CURRENT_DATE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS goals (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    titulo VARCHAR(120) NOT NULL,
    descricao VARCHAR(255),
    valor_meta NUMERIC(10,2) NOT NULL,
    valor_atual NUMERIC(10,2) NOT NULL DEFAULT 0,
    prazo DATE NOT NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'ativa',
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS educational_contents (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(140) NOT NULL,
    resumo VARCHAR(255) NOT NULL,
    conteudo TEXT NOT NULL,
    categoria VARCHAR(80) NOT NULL,
    nivel VARCHAR(30) NOT NULL DEFAULT 'iniciante',
    duracao_minutos INTEGER NOT NULL DEFAULT 5,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

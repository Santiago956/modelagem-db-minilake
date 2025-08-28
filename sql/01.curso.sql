CREATE TABLE IF NOT EXISTS curso (
    id_curso SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    descricao VARCHAR(255),
    valor DECIMAL(10, 2),
    duracao INTEGER NOT NULL
)
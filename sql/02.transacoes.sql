CREATE TABLE IF NOT EXISTS transacoes (
    id_transacao SERIAL PRIMARY KEY,
    id_curso INT NOT NULL,
    id_usuario INT NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    metodo_pagamento VARCHAR(20) NOT NULL
        CHECK(metodo_pagamento IN ('credito', 'debito', 'boleto', 'pix')),
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_curso) REFERENCES curso(id_curso),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)

)
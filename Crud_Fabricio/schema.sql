CREATE TABLE IF NOT EXISTS fretes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    caminhao TEXT NOT NULL,
    motorista TEXT NOT NULL,
    origem TEXT NOT NULL,
    destino TEXT NOT NULL,
    carga TEXT NOT NULL,
    valor REAL NOT NULL,
    status TEXT NOT NULL,
    data_entrega TEXT NOT NULL,
    criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

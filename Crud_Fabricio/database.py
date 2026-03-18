
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "fretes.db"
SCHEMA_PATH = BASE_DIR / "schema.sql"


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_connection() as conn:
        schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")
        conn.executescript(schema_sql)


def criar_frete(
    caminhao: str,
    motorista: str,
    origem: str,
    destino: str,
    carga: str,
    valor: float,
    status: str,
    data_entrega: str,
) -> int:
    sql = """
    INSERT INTO fretes (caminhao, motorista, origem, destino, carga, valor, status, data_entrega)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """

    with get_connection() as conn:
        cursor = conn.execute(
            sql,
            (caminhao, motorista, origem, destino, carga, valor, status, data_entrega),
        )
        return cursor.lastrowid


def listar_fretes() -> list[sqlite3.Row]:
    sql = "SELECT * FROM fretes ORDER BY id"

    with get_connection() as conn:
        return conn.execute(sql).fetchall()


def buscar_frete_por_id(frete_id: int) -> sqlite3.Row | None:
    sql = "SELECT * FROM fretes WHERE id = ?"

    with get_connection() as conn:
        return conn.execute(sql, (frete_id,)).fetchone()


def atualizar_frete(
    frete_id: int,
    caminhao: str,
    motorista: str,
    origem: str,
    destino: str,
    carga: str,
    valor: float,
    status: str,
    data_entrega: str,
) -> bool:
    sql = """
    UPDATE fretes
       SET caminhao = ?,
           motorista = ?,
           origem = ?,
           destino = ?,
           carga = ?,
           valor = ?,
           status = ?,
           data_entrega = ?
     WHERE id = ?
    """

    with get_connection() as conn:
        cursor = conn.execute(
            sql,
            (
                caminhao,
                motorista,
                origem,
                destino,
                carga,
                valor,
                status,
                data_entrega,
                frete_id,
            ),
        )
        return cursor.rowcount > 0


def excluir_frete(frete_id: int) -> bool:
    sql = "DELETE FROM fretes WHERE id = ?"

    with get_connection() as conn:
        cursor = conn.execute(sql, (frete_id,))
        return cursor.rowcount > 0


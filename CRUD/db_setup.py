import sqlite3

def create_database():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee TEXT NOT NULL,
            function TEXT NOT NULL,
            location TEXT NOT NULL,
            task TEXT NOT NULL,
            priority TEXT NOT NULL,
            status TEXT NOT NULL,
            start_date TEXT,
            end_date TEXT,
            responsible TEXT NOT NULL,
            created_date TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
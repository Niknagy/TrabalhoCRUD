import sqlite3

def insert_task(employee, function, location, task, priority, status, start_date, end_date, responsible):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (employee, function, location, task, priority, status, start_date, end_date, responsible)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (employee, function, location, task, priority, status, start_date, end_date, responsible))
    conn.commit()
    conn.close()

def get_all_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task(id, employee, function, location, task, priority, status, start_date, end_date, responsible):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE tasks SET employee=?, function=?, location=?, task=?, priority=?, status=?, start_date=?, end_date=?, responsible=?
        WHERE id=?
    ''', (employee, function, location, task, priority, status, start_date, end_date, responsible, id))
    conn.commit()
    conn.close()

def delete_task(id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id=?', (id,))
    conn.commit()
    conn.close()

def search_tasks(query):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE task LIKE ? OR employee LIKE ?', ('%' + query + '%', '%' + query + '%'))
    tasks = cursor.fetchall()
    conn.close()
    return tasks
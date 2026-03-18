from flask import Flask, render_template, request, redirect, url_for
import crud
import db_setup

app = Flask(__name__)
db_setup.create_database()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        crud.insert_task(
            request.form['employee'],
            request.form['function'],
            request.form['location'],
            request.form['task'],
            request.form['priority'],
            request.form['status'],
            request.form['start_date'],
            request.form['end_date'],
            request.form['responsible']
        )
        return redirect(url_for('list_tasks'))
    return render_template('insert.html')

@app.route('/list')
def list_tasks():
    tasks = crud.get_all_tasks()
    return render_template('list.html', tasks=tasks)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        crud.update_task(
            id,
            request.form['employee'],
            request.form['function'],
            request.form['location'],
            request.form['task'],
            request.form['priority'],
            request.form['status'],
            request.form['start_date'],
            request.form['end_date'],
            request.form['responsible']
        )
        return redirect(url_for('list_tasks'))
    task = crud.get_all_tasks()
    task = next((t for t in task if t[0] == id), None)
    return render_template('update.html', task=task)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    if request.method == 'POST':
        crud.delete_task(id)
        return redirect(url_for('list_tasks'))
    task = crud.get_all_tasks()
    task = next((t for t in task if t[0] == id), None)
    return render_template('delete.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)
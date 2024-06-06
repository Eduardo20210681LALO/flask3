from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Lista de tareas
tasks = []

@app.route('/')
def home():
    return render_template('Index.html')

# Listar todas las tareas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Agregar una nueva tarea
@app.route('/tasks', methods=['POST'])
def add_task():
    task_data = request.get_json()
    task = task_data.get('task')
    tasks.append(task)
    return f"Tarea '{task}' agregada correctamente.\n"

# Eliminar una tarea
@app.route('/tasks/<int:index>', methods=['DELETE'])
def delete_task(index):
    if index < len(tasks):
        deleted_task = tasks.pop(index)
        return f"Tarea '{deleted_task}' eliminada correctamente.\n"
    else:
        return "Índice de tarea fuera de rango.\n"

if __name__ == '__main__':
    app.run(debug=True)

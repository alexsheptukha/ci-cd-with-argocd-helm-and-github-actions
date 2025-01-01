""" Простое приложение todo """
from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = []
@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Получаем все задачи
    """
    return jsonify({'tasks': tasks})
# Получение отдельной задачи
@app.route('/tasks', methods=['POST'])
def add_task():
    """
    Добавление задачи
    """
    task = {
      'id': len(tasks) + 1,
      'title': request.json['title'],
      'description': request.json['description'],
    }
    tasks.append(task)
    return jsonify(task), 201
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

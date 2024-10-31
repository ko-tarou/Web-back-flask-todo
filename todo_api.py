from flask import Flask, jsonify, request

app = Flask(__name__)

# サンプルデータ（TODOリスト）
todos = [
    {"id": 1, "task": "Buy groceries", "done": False},
    {"id": 2, "task": "Read a book", "done": False},
]

# TODOリストの全項目を取得する
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# TODO項目を取得する
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((item for item in todos if item["id"] == todo_id), None)
    if todo:
        return jsonify(todo)
    return jsonify({"error": "Todo not found"}), 404

# TODO項目を追加する
@app.route('/todos', methods=['POST'])
def add_todo():
    if not request.json or 'task' not in request.json:
        return jsonify({"error": "Invalid input"}), 400
    new_todo = {
        "id": len(todos) + 1,
        "task": request.json['task'],
        "done": request.json.get('done', False)
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

# TODO項目を更新する
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((item for item in todos if item["id"] == todo_id), None)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    if not request.json:
        return jsonify({"error": "Invalid input"}), 400

    todo['task'] = request.json.get('task', todo['task'])
    todo['done'] = request.json.get('done', todo['done'])
    return jsonify(todo)

# TODO項目を削除する
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [item for item in todos if item["id"] != todo_id]
    return jsonify({"message": "Todo deleted successfully"})

# サーバーを起動する
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)

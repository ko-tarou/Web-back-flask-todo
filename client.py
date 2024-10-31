import requests
import json

BASE_URL = "http://127.0.0.1:5000"  # FlaskサーバーのURL（ローカルホスト）

# TODOリストの全項目を取得（GETリクエスト）
response = requests.get(f"{BASE_URL}/todos")
print("GET /todos:", response.status_code, response.json())

# 新しいTODO項目を追加（POSTリクエスト）
new_todo = {"task": "Write some code"}
response = requests.post(f"{BASE_URL}/todos", json=new_todo)
print("POST /todos:", response.status_code, response.json())

# 特定のTODO項目を取得（GETリクエスト）
todo_id = 1
response = requests.get(f"{BASE_URL}/todos/{todo_id}")
print(f"GET /todos/{todo_id}:", response.status_code, response.json())

# 特定のTODO項目を更新（PUTリクエスト）
update_data = {"task": "Buy groceries and cook dinner", "done": True}
response = requests.put(f"{BASE_URL}/todos/{todo_id}", json=update_data)
print(f"PUT /todos/{todo_id}:", response.status_code, response.json())

# 特定のTODO項目を削除（DELETEリクエスト）
response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
print(f"DELETE /todos/{todo_id}:", response.status_code, response.json())

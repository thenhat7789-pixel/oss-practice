from flask import Flask, jsonify, request, send_from_directory
import os

app = Flask(__name__, static_folder='.')

tasks = [
    {"id": 101, "name": "Thiết lập Flask Web Server trong Python 3.11", "env": "Windows & Ubuntu", "status": "Hoàn Thành"},
    {"id": 102, "name": "Xây dựng giao diện Bài 6 (index6.html)", "env": "Frontend HTML/CSS", "status": "Hoàn Thành"},
    {"id": 103, "name": "Tích hợp REST API Bài 7 (index7.html)", "env": "Python Flask API", "status": "Hoàn Thành"},
    {"id": 104, "name": "Đồng bộ Git Repository 2 chiều lên GitHub", "env": "Git / GitHub", "status": "Hoàn Thành"}
]

@app.route('/')
def home():
    return send_from_directory('.', 'index6.html')

@app.route('/<path:filename>')
def serve_file(filename):
    if os.path.exists(filename):
        return send_from_directory('.', filename)
    return "File Not Found", 404

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"success": True, "count": len(tasks), "data": tasks})

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.json or {}
    new_task = {
        "id": 100 + len(tasks) + 1,
        "name": data.get("name", "Nhiệm vụ mới"),
        "env": "Python Backend",
        "status": "Hoàn Thành"
    }
    tasks.append(new_task)
    return jsonify({"success": True, "task": new_task})

if __name__ == '__main__':
    print("==================================================")
    print("🚀 Python Web Server is running on http://127.0.0.1:5000")
    print("📌 Bài Tập 6: http://127.0.0.1:5000/index6.html")
    print("📌 Bài Tập 7: http://127.0.0.1:5000/index7.html")
    print("==================================================")
    app.run(host='0.0.0.0', port=5000, debug=True)

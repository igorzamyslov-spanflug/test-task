from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

todos = []


@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)


@app.route("/todos", methods=["POST"])
def add_todo():
    todo = request.json.get("todo")
    todos.append(todo)
    return jsonify(todo)


if __name__ == "__main__":
    app.run(debug=True, port=7999)

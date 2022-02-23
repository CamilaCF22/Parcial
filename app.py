from flask import Flask, render_template, request, redirect, url_for
from db.dbusers import selectAllUsers, insertNewUser, selectUserById, updateUser, deleteUser
from db.dbstatus import selectAllStatus, insertNewStatus, selectStatusById, updateStatus, deleteStatus
from db.dbtasks import selectAllTasksByUser, insertNewTask, selectTaskById, updateTask, deleteTask
from models.user import User
from models.status import Status
from models.task import Task

app = Flask(__name__)


@app.route("/")
def home():
    return "home"


@app.route("/users/show")
def show_users():
    return "show users"


@app.route("/users/new", methods=["POST"])
def new_user():
    return "new user"


@app.route("/users/update/<int:id>", methods=["GET", "POST"])
def update_user(id):
    return "update user"


@app.route("/users/delete/<int:id>")
def delete_user(id):
    return "delete user"


@app.route("/status/show")
def show_status():
    return "show status"


@app.route("/status/new", methods=["POST"])
def new_status():
    return "new status"


@app.route("/status/update/<int:id>", methods=["GET", "POST"])
def update_status(id):
    return "update status"


@app.route("/status/delete/<int:id>")
def delete_status(id):
    return "delete status"


@app.route("/tasks/user")
def task_select_user():
    return "task select user"


@app.route("/tasks/show/<int:iduser>", methods=["GET", "POST"])
def show_tasks(iduser):
    return "show tasks"


@app.route("/tasks/new/<int:iduser>", methods=["GET", "POST"])
def new_task(iduser):
    return "new task"


@app.route("/tasks/update/<int:iduser>/<int:id>", methods=["GET", "POST"])
def update_task(iduser, id):
    return "update task"


@app.route("/tasks/delete/<int:iduser>/<int:id>")
def delete_task(iduser, id):
    return "delete task"


if __name__ == "__main__":
    app.run(debug=True)

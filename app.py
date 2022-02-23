from flask import Flask, render_template, request, redirect, url_for
from db.dbusers import selectAllUsers, insertNewUser, selectUserById, updateUser, deleteUser
from db.dbstatus import selectAllStatus, insertNewStatus, selectStatusById, updateStatus, deleteStatus
from db.dbtasks import selectAllTasks, selectAllTasksByUser, insertNewTask, selectTaskById, updateTask, deleteTask
from models.user import User
from models.status import Status
from models.task import Task

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")
    return redirect (url_for("home"))

@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/users/show")
def show_users():
    users=selectAllUsers()
    return render_template("show.html", users=users)


@app.route("/users/new", methods=["POST"])
def new_user():
    if request.method == "GET":
        return render_template("show.html")
    elif request.method == "POST":
        name = request.form.get("name")
        insertNewUser(user)
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))



@app.route("/users/update/<int:id>", methods=["GET", "POST"])
def update_user(id):
    if request.method == "GET":
        user = selectPersonBy(id)
        return render_template("update.html", user=user)
    elif request.method == "POST":
        name = request.form.get("name")
        updateUser(user)
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


@app.route("/users/delete/<int:id>")
def delete_user(id):
    deleteUser(id)
    return redirect(url_for("home"))


@app.route("/status/show")
def show_status():
    statusList=selectAllStatus()
    return render_template("show.html", statusList=statusList)


@app.route("/status/new", methods=["POST"])
def new_status():
    if request.method == "GET":
        return render_template("show.html")
    elif request.method == "POST":
        name = request.form.get("name")
        insertNewStatus(status)
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))



@app.route("/status/update/<int:id>", methods=["GET", "POST"])
def update_status(id):
    if request.method == "GET":
        status = selectStatusById(id)
        return render_template("update.html", status=status)
    elif request.method == "POST":
        name = request.form.get("name")
        updateStatus(status)
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


@app.route("/status/delete/<int:id>")
def delete_status(id):
    deleteStatus(id)
    return redirect(url_for("home"))


@app.route("/tasks/user")
def task_select_user():
    select=selectAllTasksByUser(iduser)
    return render_template("selectUser.html", select=select)


@app.route("/tasks/show/<int:iduser>", methods=["GET", "POST"])
def show_tasks(iduser):
    taks=selectAllTasks()
    return render_template("show.html", tasks=tasks)


@app.route("/tasks/new/<int:iduser>", methods=["GET", "POST"])
def new_task(iduser):
    if request.method == "GET":
        return render_template("new.html")
    elif request.method == "POST":
        description = request.form.get("description")
        status = request.form.get("status")
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))

@app.route("/tasks/update/<int:iduser>/<int:id>", methods=["GET", "POST"])
def update_task(iduser, id):
    if request.method == "GET":
        task = selectAllTasksByUser(iduser)
        return render_template("update.html", task=task)
    elif request.method == "POST":
        description = request.form.get("description")
        status = request.form.get("status")
        updateTask(task)
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


@app.route("/tasks/delete/<int:iduser>/<int:id>")
def delete_task(iduser, id):
    deleteTask(id)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

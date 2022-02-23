from db.dbconnection import createDBConnection
from models.task import Task


def selectAllTasks():
    connection = createConnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM specialtodolistdb.tasks;"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


def selectAllTasksByUser(iduser):
    connection = createConnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM specialtodolistdb.tasks where id=%s;"
            cursor.execute(sql, id)
            result = cursor.fetchone()
            return result


def insertNewTask(task: Task):
    connection = createConnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `specialtodolist`.`tasks` (`id`,`iduser`,`description`,`idstatus`)VALUES (%s, %s, %s, %s);"
            cursor.execute(sql, (0, 0, task.description, 0))
        connection.commit()


def selectTaskById(id) -> dict:
    connection = createConnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM specialtodolist.tasks where id=%s;"
            cursor.execute(sql, id)
            result = cursor.fetchone()
            return result


def updateTask(task: Task):
    connection = createConnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE `specialtodolist`.`tasks` SET `iduser` = %s, `description` = %s, `idstatus` = %s, = WHERE `id` = %s;"
            cursor.execute(sql, (task.iduser,task.description, task.idstatus, task.id))
        connection.commit()


def deleteTask(id: int):
    connection = createConnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `specialtodolist`.`tasks` WHERE id=%s;"
            cursor.execute(sql, id)
        connection.commit()
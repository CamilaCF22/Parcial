from db.dbconnection import createDBConnection
from models.user import User


def selectAllUsers():
    connection = createConnectionToDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM specialtodolistdb.users;"
            cursor.execute(sql)
            result = cursor.fetchall()
        return result


def insertNewUser(user: User):
    connection = createConnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `specialtodolist`.`users` (`id`,`name`)VALUES (%s, %s);"
            cursor.execute(sql, (0, user.name))
        connection.commit()


def selectUserById(id) -> dict:
    connection = createConnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM specialtodolist.users where id=%s;"
            cursor.execute(sql, id)
            result = cursor.fetchone()
            return result


def updateUser(user: User):
    connection = createConnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE `specialtodolist`.`user` SET `name` = %s WHERE `id` = %s;"
            cursor.execute(sql, (person.name, person.id))
        connection.commit()



def deleteUser(id: int):
    connection = createConnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `specialtodolist`.`user` WHERE id=%s;"
            cursor.execute(sql, id)
        connection.commit()

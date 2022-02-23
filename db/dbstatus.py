from db.dbconnection import createDBConnection
from models.status import Status


def selectAllStatus():
    connection = createConnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM specialtodolistdb.status;"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


def insertNewStatus(status: Status):
    connection = createConnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `specialtodolistdb`.`status` (`id`,`name`)VALUES (%s, %s);"
            cursor.execute(sql, (0, person.name))
        connection.commit()


def selectStatusById(id) -> dict:
    connection = createConnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM specialtodolistdb.status where id=%s;"
            cursor.execute(sql, id)
            result = cursor.fetchone()
            return result


def updateStatus(status: Status):
    connection = createConnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE `specialtodolistdb`.`statys` SET `name` = %s WHERE `id` = %s;"
            cursor.execute(sql, (person.name, person.id))
        connection.commit()

def deleteStatus(id: int):
    connection = createConnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `specialtodolistdb`.`status` WHERE id=%s;"
            cursor.execute(sql, id)
        connection.commit()

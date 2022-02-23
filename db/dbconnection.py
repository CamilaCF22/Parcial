import pymysql.cursors

def createConnectionToDB():
	    connection = pymysql.connect(
	        host="localhost",
	        user="root",
	        password="root",
	        database="specialtodolistdb",
	        port=3306,
	        cursorclass=pymysql.cursors.DictCursor,
	    )
	    return connection
 

    

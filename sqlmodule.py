import mysql.connector as sqlctr



def connect_server(pw):
    connection = None
    try:
        connection = sqlctr.connect(
            host="localhost",
            user="root",
            password=pw
        )
    except:
        print("Incorrect Password")
    return connection, pw


def connect_database(pasword):
    connection = None
    try:
        connection = sqlctr.connect(
            host="localhost",
            user="root",
            password=pasword,
            database="gnps21_db"
        )
    except:
        pass
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()


def read_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result



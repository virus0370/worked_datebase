import pymysql


with pymysql.connect(host="localhost", port=3307, user="root", password="") as connection:
    print(connection, "OK")



def create_datebase(cursor, connection):
    try:
        db_name= input("insert a name: ")
        query = f"""CREATE DATABASE IF NOT EXISTS {db_name} """
        cursor.execute(query)
        connection.commit()
        if input("Would you change current base ti this new database(yse or no): ").lower() in ("yes","y"):
            query = f"""USE {db_name}"""
            cursor.execute(query)
            print(f"Using datebase:{db_name}")
    except:
        print("no, sorry, they have wekeand")


def craete_table(cursor, connection):
    try:
        table_name = input("Name of table: ")
        column_name = input("test column name: ")
        second_column_name = input("second column name: ")
        query = f"""CREATE TABLE IF NOT EXISTS {table_name} ({column_name} INT PRIMARY KEY, {second_column_name} VARCHAR(255))"""
        cursor.execute(query)
        connection.commit()
    except:
        print("no, sorry, they have wekeand")


def insert_info(cursor, connection):
    show_all_tables()
    table = input("name of table: ")
    try:
        query = f"""SHOW COLUMNS FROM {table}"""
        cursor.execute(query)
        print("all colums: ")
        for column in cursor:
            print(*column)
        match table:
            case"teachers":
                query = """INSERT INTO teachers (first_name, second_name,age) VALUES (%s, %s, %s)"""
                values = (
                    input('Insert a first name: '),
                    input('Insert a second name: '),
                    int(input('Insert a age: ')),
                )
                cursor.execute(query, values)
                connection.commit()
            case"groups":
                query = """INSERT INTO groups (name, auditory) VALUES (%s, %s)"""
                values = (
                    input('Insert a first name: '),
                    input('Insert a auditory: ')
                )
                cursor.execute(query, values)
                connection.commit()
            case "teacher_and_groups":
                query = f"""SELECT * FROM TEACHERS"""
                cursor.execute(query)
                for teacher in cursor:
                    print(f"id: {teacher[0]}; firstname {teacher[1]}; lastname{teacher[2]}")
                theachers_id = input('Insert theacher id: ')

                query = f"""SELECT * FROM GROUPS"""
                cursor.execute(query)
                for groups in cursor:
                    print(f"id: {groups[0]}; name {groups[1]}; auditori{groups[2]}")
                groups_id = input('Insert groups id: ')


                query = """INSERT INTO teachers_and_groups (theacher_id, groups_id) VALUES (%s, %s)"""

                values = (theachers_id, groups_id)

                cursor.execute(query, values)
                connection.commit()
    except:
        print("no, sorry, they have wekeand")


def delete_info(cursor, connection):
    try:
        show_all_tables()
        table= input("select table: ")
        query = f"""SELECT * FROM {table}"""
        cursor.execute(query)
        print("all colums: ")
        for column in cursor:
            print(*column)

        values = int(input("your field id: "))
        query = f"""DELETE FROM {table} WHERE id = %s"""


        cursor.execute(query, values)
        connection.commit()
    except:
        print("no, sorry, they have wekeand")


def update_info(cursor, connection):
    teacher_id  = int(input("teacher_id: "))
    query = f"""UPDATE theachers SET first_name = %s, second_name = %s, age = %s WHERE id = {teacher_id}"""
    values = (input("firstname: "), ("second name: "), int(input("age: ")))
    cursor.execute(query,values)
    connection.commit()


def show_all_databases(cursor):
    try:
        cursor.execute("SHOW DATABASES")
        print("all databases")
        for db in cursor:
            print(*db)
    except:
        print("no, sorry, they have weakeand")


def show_all_tables(cursor):
    try:
        cursor.execute("SHOW TABLES")
        print("all tables this database")
        for db in cursor:
            print(*db)
    except:
        print("no, sorry, they have weakeand")


def show_all_columns(cursor, connection):
    try:
        Table_name=input("your tables? : ")
        query = f"""SHOW COLUMNS FROM {Table_name}"""
        cursor.execute(query)
        for db in cursor:
            print(*db)
    except:
        print("no, sorry, they have weakeand")


def show_all_dataInTables(cursor, connection):
    try:
        tables= "SHOW TABLES"
        cursor.execute(tables)
        for db in cursor:
            print(*db)
        Table_name=input("your tables? : ")
        query = f"""SELECT * FROM {Table_name}"""
        cursor.execute(query)
        for db in cursor:
            print(*db)
    except:
        print("no, sorry, they have weakeand")


def change_database(cursor, connection):
    try:
        query = f"""USE {input("insert a name: ")} """
        cursor.execute(query)
        print('Done.')
    except:
        print("no, sorry, they have weakeand")


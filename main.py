import pymysql

def create_datebase():
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


def craete_table():
    try:
        table_name = input("Name of table: ")
        column_name = input("test column name: ")
        second_column_name = input("second column name: ")
        query = f"""CREATE TABLE IF NOT EXISTS {table_name} ({column_name} INT PRIMARY KEY, {second_column_name} VARCHAR(255))"""
        cursor.execute(query)
        connection.commit()
    except:
        print("no, sorry, they have wekeand")


def insert_info():
    pass


def delete_info():
    pass


def update_info():
    pass


def show_info():
    print("1. Show all date bases.")
    print("2. Show all tables in current datebase.")
    print("3. Show all colums in some table.")
    print("4. Show all data in some table.")
    print("5. Show all others info.")
    print("6. back.")
    user_choise= input("your choise: ")


def change_database():
    try:
        query = f"""USE {input("insert a name: ")} """
        cursor.execute(query)
        print('Done.')
    except:
        print("no, sorry, they have weakeand")


try:
    with pymysql.connect(host="localhost", port=3307, user="root", password="") as connection:
        print(connection, "OK")
        with connection.cursor() as cursor:
            # # cursor.execute("SHOW DATABASES")
            # # for db in cursor:
            # #     print(db)
            # #
            # # cursor.execute("CREATE DATABASE IF NOT EXISTS TESTIK")
            # #
            # # print("-------------")
            # # cursor.execute("SHOW DATABASES")
            # # for db in cursor:
            # #     print(db)
            # cursor.execute("CREATE DATABASE IF NOT EXISTS ACADEMY")
            cursor.execute("USE ACADEMY")

            # cursor.execute(
            #     """
            #     CREATE TABLE IF NOT EXISTS teachers (
            #         id INT AUTO_INCREMENT PRIMARY KEY,
            #         first_name VARCHAR(100),
            #         second_name VARCHAR(100),
            #         age INT
            #     )
            #     """
            # )
            # cursor.execute(
            #     """
            #     CREATE TABLE IF NOT EXISTS groups (
            #         id INT AUTO_INCREMENT PRIMARY KEY,
            #         name VARCHAR(100),
            #         auditory VARCHAR(10)
            #     )
            #     """
            # )
            # cursor.execute(
            #     """
            #     CREATE TABLE IF NOT EXISTS teachers_and_groups (
            #         teacher_id INT,
            #         group_id INT,
            #         PRIMARY KEY(teacher_id, group_id),
            #         FOREIGN KEY (teacher_id) REFERENCES teachers(id),
            #         FOREIGN KEY (group_id) REFERENCES groups(id)
            #     )
            #     """
            # )
            # cursor.execute("Use Academy")
            # cursor.execute(
            #     """INSERT INTO teachers(first_name)"""
            # )
            cursor.execute("USE ACADEMY")
            while True:
                print("1. create database")
                print("2. change database")
                print("3. create table")
                print("4. insert info")
                print("5. delete info")
                print("6. update info")
                print("7. show info")
                print("0. exit")
                user_choise = input("you choice: ")
                match user_choise:
                    case "1": create_datebase()
                    case "2":
                        change_database()
                    case "3":
                        craete_table()
                    case "4":
                        insert_info()
                    case "5":
                        delete_info()
                    case "6":
                        update_info()
                    case "7":
                        show_info()
                    case "0":
                        quit()
                    case "_":
                        print("Unknown command.")


except pymysql.Error as e:
    print(e)
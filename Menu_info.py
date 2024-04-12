import pymysql
import Database_operation as Oper

with pymysql.connect(host="localhost", port=3307, user="root", password="") as connection:
    print(connection, "OK")
    with connection.cursor() as cursor:
        cursor.execute("USE ACADEMY")

def show_info(cursor, connection):
    print("1. Show all date bases.")
    print("2. Show all tables in current datebase.")
    print("3. Show all colums in some table.")
    print("4. Show all data in some table.")
    print("5. Show all others info.")
    print("6. back.")
    user_choise= input("your choise: ")
    match user_choise:
        case"1": Oper.show_all_databases(cursor)
        case "2":
            Oper.show_all_tables(cursor)
        case "3":
            Oper.show_all_columns(cursor, connection)
        case "4":
            Oper.show_all_dataInTables(cursor, connection)
        case "5":
            """SHOW DATABASES"""
        case "0":
            return
        case "_":
            print("no, sorry, they have weakeand")



import pymysql
import Database_operation
import Menu_info
Oper = Database_operation
menu = Menu_info
try:
    with pymysql.connect(host="localhost", port=3307, user="root", password="") as connection:
        print(connection, "OK")
        with connection.cursor() as cursor:

            cursor.execute("USE ACADEMY")
            while True:
                print("\n\n")
                print("=" * 80)
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
                    case "1": Oper.create_datebase(cursor, connection)
                    case "2":
                        Oper.change_database(cursor, connection)
                    case "3":
                        Oper.craete_table(cursor, connection)
                    case "4":
                        Oper.insert_info(cursor, connection)
                    case "5":
                        Oper.delete_info(cursor, connection)
                    case "6":
                        Oper.update_info(cursor, connection)
                    case "7":
                        menu.show_info(cursor, connection)
                    case "0":
                        quit()
                    case "_":
                        print("Unknown command.")


except pymysql.Error as e:
    print(e)
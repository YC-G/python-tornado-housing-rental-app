import pymysql
import config

def main():
    connection = pymysql.connect(**config.mysql_options)

    try:
        cursor = connection.cursor()
        new_database_name = "iHome"
        create_database_query = f"CREATE DATABASE {new_database_name}"
        cursor.execute(create_database_query)
        connection.commit()
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    main()
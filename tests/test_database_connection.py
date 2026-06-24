import os
import pymysql


def test_sakila_database_connection():
    connection = pymysql.connect(
        host=os.environ.get("MYSQL_HOST", "db"),
        user=os.environ.get("MYSQL_USER", "root"),
        password=os.environ.get("MYSQL_PASSWORD", "admin"),
        database=os.environ.get("MYSQL_DB", "sakila"),
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM actor;")
            result = cursor.fetchone()
            assert result[0] > 0
    finally:
        connection.close()

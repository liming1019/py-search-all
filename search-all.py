import pymssql
import os

conn = pymssql.connect(server="172.20.2.12", user="lm", password="123", database="Rkylin_ERP", port="30000", charset="utf8")
cursor = conn.cursor()
sql = "select  name,server,user_1,password,database_1,port,charset from t_PYTHON_LINJIASEN"
try:
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount <= 0:
        exit(0)
    for row in result:
        try:
            child_conn = pymssql.connect(server=row[1], user=row[2], password=row[3], database=row[4], port=row[5],
                                         charset="utf8")
            try:
                file_path = os.path.dirname(os.path.realpath(__file__)) + "/file.sql"
                f = open(file_path, "r")
                child_sql = f.read()
                print f.read()
            except Exception as e:
                print(e)
                exit(0)
            finally:
                if f:
                    f.close()
            child_cursor = child_conn.cursor()
            child_cursor.execute(child_sql)
            child_result = child_cursor.fetchall()

            if child_cursor.rowcount <= 0:
                print("%s %s" % (row[0], "no this data"))

            for child_row in child_result:
                print("%s %s" % (row[0], child_row[0]))
        except Exception as ec:
            print(ec)
        finally:
            child_cursor.close()
except Exception as e:
    print(e)
finally:
    cursor.close()

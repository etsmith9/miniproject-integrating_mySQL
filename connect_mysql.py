import mysql.connector
from mysql.connector import Error


def connect_database():
    # database connection parameters
    db_name = "LIBRARY_MANAGEMENT_SYSTEM"
    user = "root"
    password = "amrit101!"
    host = "localhost"

    try:
        #Attemping to establish a connection
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )

        #check if the connection is successful
        print("Connected to MySQL database successfully")
        return conn

    except Error as e:
        #hangling any connection errors
        print(f"Error: {e}")
        return None


#     #SQL query
#     query = "SELECT * FROM Customers"

#     #executing the query
#     cursor.execute(query)

#     #fetching the results
#     for row in cursor.fetchall():
#         print(row)
# except Error as e:
#     print(f"Error: {e}")

# finally:
#     if conn and conn.is_connected():
#         cursor.close()
#         conn.close()

def main():
    print("here")
    connect_database()

if __name__ == "__main__":
    main()
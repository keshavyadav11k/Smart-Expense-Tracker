import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="set"
    )

    cursor = connection.cursor()

    # Example: user_id is DOUBLE
    insert_query = "INSERT INTO users (name, username, email, password) VALUES ( %s,%s, %s, %s)"
    
    # Data to insert
    data = ('keshav2', "test_user2", "test2@example.com", "secret2")  # user_id as float

    cursor.execute(insert_query, data)
    connection.commit()

    print("✅ Record inserted successfully!")

except mysql.connector.Error as err:
    print("MySQL Error:", err)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()

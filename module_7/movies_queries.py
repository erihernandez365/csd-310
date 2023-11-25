import mysql.connector

try:
    # Establishing a connection to the MySQL database
    mydb = mysql.connector.connect(
        host="DESKTOP-JPE14IK",
        user="root",
        password="ChicagoPD!311",
        database="movies"
    )

    # Creating a cursor object using the cursor() method
    cursor = mydb.cursor()

    # Query 1: Select studio records
    query_studio = "SELECT Studio_ID, Studio_Name FROM Studio;"
    cursor.execute(query_studio)
    studio_records = cursor.fetchall()

    # Displaying Studio Records
    print("-- DISPLAYING Studio Records --")
    for record in studio_records:
        print("Studio ID:", record[0])
        print("Studio Name:", record[1])
        print()

    # Similarly, perform operations for other queries and display data

    # Closing the cursor and database connection
    cursor.close()
    mydb.close()

except mysql.connector.Error as error:
    print("Error occurred:", error)

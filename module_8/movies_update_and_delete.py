import mysql.connector

def connect_to_movies_database():
    try:
        # Establishing a connection to the movies database
        mydb = mysql.connector.connect(
            user="root",
            password="ChicagoPD!311",
            database="movies"
        )

        # Cursor object
        return mydb.cursor()

    except mysql.connector.Error as error:
        print("Error occurred while connecting to the database:", error)
        return None  # Return None in case of an error
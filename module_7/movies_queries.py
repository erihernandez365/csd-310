import mysql.connector

try:
    # Establishing a connection to the MySQL database
    mydb = mysql.connector.connect(
        user="root",
        password="ChicagoPD!311",
        database="movies"
    )

    # Creating a cursor object using the cursor() method
    cursor = mydb.cursor()

    # Query 3: Selecting short films with their runtime
    query_short_films = "SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;"
    cursor.execute(query_short_films)
    short_film_records = cursor.fetchall()

    # Displaying Short Film Records
    print("-- DISPLAYING Short Film RECORDS --")
    for record in short_film_records:
        print("Film Name:", record[0])
        print("Runtime:", record[1])
        print()

    # Query 4: Selecting film names and directors ordered by director
    query_directors = "SELECT film_name, film_director FROM film ORDER BY film_director;"
    cursor.execute(query_directors)
    director_records = cursor.fetchall()

    # Displaying Director Records
    print("-- DISPLAYING Director of RECORDS in Order --")
    for record in director_records:
        print("Film Name:", record[0])
        print("Director:", record[1])
        print()

    # Closing the cursor and database connection
    cursor.close()
    mydb.close()

except mysql.connector.Error as error:
    print("Error occurred:", error)
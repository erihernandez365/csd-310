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

    # Query 2: Select genre records
    query_genre = "SELECT Genre_ID, Genre_Name FROM Genre;"
    cursor.execute(query_genre)
    genre_records = cursor.fetchall()

    # Displaying Genre Records
    print("-- DISPLAYING Genre RECORDS --")
    for record in genre_records:
        print("Genre ID:", record[0])
        print("Genre Name:", record[1])
        print()

    # Query 3: Select short films with runtime less than two hours
    query_short_films = "SELECT Film_Name, Runtime FROM Films WHERE Runtime < 120;"
    cursor.execute(query_short_films)
    short_film_records = cursor.fetchall()

    # Displaying Short Film Records
    print("-- DISPLAYING Short Film RECORDS --")
    for record in short_film_records:
        print("Film Name:", record[0])
        print("Runtime:", record[1])
        print()

    # Query 4: Select film names and directors ordered by director
    query_director = "SELECT Film_Name, Director FROM Films ORDER BY Director;"
    cursor.execute(query_director)
    director_records = cursor.fetchall()

    # Displaying Director of Records in Order
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

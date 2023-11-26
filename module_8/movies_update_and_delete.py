import mysql.connector

def show_films(cursor, title):
    select_query = (
        "SELECT film_name as 'Film Name', film_director as 'Director', "
        "genre_name as 'Genre Name ID', studio_name as 'Studio Name' "
        "FROM film "
        "INNER JOIN genre ON film.genre_id = genre.genre_id "
        "INNER JOIN studio ON film.studio_id = studio.studio_id"
    )
    cursor.execute(select_query)
    films = cursor.fetchall()

    print(f"-- {title} --")
    for film in films:
        print(f"Film Name: {film[0]}\nDirector: {film[1]}\nGenre Name ID: {film[2]}\nStudio Name: {film[3]}\n")

# Establish connection to MySQL
connection = mysql.connector.connect(
    user="root",
    password="ChicagoPD!311",
    database="movies"
)
cursor = connection.cursor()

# Call the function to display films
show_films(cursor, "DISPLAYING FILMS")

# Insert a new record for the movie "Inception"
insert_query = "INSERT INTO film (film_name, film_director, genre_id, studio_id, film_releaseDate, film_runtime) VALUES (%s, %s, %s, %s, %s, %s)"
insert_values = ("Inception", "Christopher Nolan", 1, 1, "2010", 148)
cursor.execute(insert_query, insert_values)
connection.commit()

# Call the function to display films after insert
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# Update the genre of the movie "Alien" to Horror
update_query = "UPDATE film SET genre_id = %s WHERE film_name = %s"
update_values = (3, "Alien")
cursor.execute(update_query, update_values)
connection.commit()

# Call the function to display films after update
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

# Delete the movie "Gladiator"
delete_query = "DELETE FROM film WHERE film_name = %s"
delete_values = ("Gladiator",)
cursor.execute(delete_query, delete_values)
connection.commit()

# Call the function to display films after delete
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

# Close connection
cursor.close()
connection.close()
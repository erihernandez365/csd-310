import mysql.connector

# Establish a connection
mydb = mysql.connector.connect(
    user="root",
    password="ChicagoPD!311",
    database="movies"
)

# Create a cursor
cursor = mydb.cursor()

# Function to display films
def show_films(cursor, title):
    sql = "SELECT film_name as 'Film Name', film_director as 'Director', genre_name as 'Genre', studio_name as 'Studio' " \
          "FROM film " \
          "INNER JOIN genre ON film.genre_id = genre.genre_id " \
          "INNER JOIN studio ON film.studio_id = studio.studio_id"
    cursor.execute(sql)
    films = cursor.fetchall()
    print(f"-- {title} --")
    for film in films:
        print(f"Film Name: {film[0]}\nDirector: {film[1]}\nGenre: {film[2]}\nStudio: {film[3]}\n")
    print("\n")

# Call the function to display films
show_films(cursor, "DISPLAYING FILMS")
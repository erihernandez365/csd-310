import mysql.connector

# Establish connection to MySQL
mydb = mysql.connector.connect(
    host="DESKTOP-JPE14IK",
    user="root",
    password="ChicagoPD!311",
    database="movies"
)

# Function to execute queries and display results
def execute_query(query, description):
    print(f"-- DISPLAYING {description} RECORDS --")
    cursor = mydb.cursor()
    cursor.execute(query)
    for result in cursor.fetchall():
        print(*result, sep='\n')
    print()

# Query 1: Select all fields for the studio table
query1 = "SELECT * FROM studio"
execute_query(query1, "Studio")

# Query 2: Select all fields for the genre table
query2 = "SELECT * FROM genre"
execute_query(query2, "Genre")

# Query 3: Select movie names for movies with a run time of less than two hours
query3 = "SELECT film_name, runtime FROM movies WHERE runtime < 120"
execute_query(query3, "Short Film")

# Query 4: Get a list of film names and directors ordered by director
query4 = "SELECT film_name, director FROM movies ORDER BY director"
execute_query(query4, "Director of Films in Order")

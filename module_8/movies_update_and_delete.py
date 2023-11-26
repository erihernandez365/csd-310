import mysql.connector

# Function to connect to the movies database
def connect_to_movies_database():
    try:
        # Establishing a connection to the movies database
        mydb = mysql.connector.connect(
            user="root",
            password="ChicagoPD!311",
            database="movies"
        )

        # Creating a cursor object from the connection
        return mydb.cursor()

    except mysql.connector.Error as error:
        print("Error occurred while connecting to the database:", error)
        return None  # Return None in case of an error

# Function to display films
def show_films(cursor, title):
    try:
        # Execute SELECT query to display films
        # Use cursor.execute() to execute your query here
        
        # Fetch all the results
        films = cursor.fetchall()

        # Display films with the provided title
        print(f"-- {title} --")
        for film in films:
            print(f"Film Name: {film[0]}")
            print(f"Director: {film[1]}")
            print(f"Genre Name ID: {film[2]}")
            print(f"Studio Name: {film[3]}\n")

    except mysql.connector.Error as error:
        print("Error occurred while fetching films:", error)

# Main function to perform tasks
def main():
    # Connect to the movies database
    cursor = connect_to_movies_database()

    if cursor:
        # Display films initially
        show_films(cursor, "DISPLAYING FILMS")

        try:
            # Insert a new record
            # Use cursor.execute() to insert a new record into the film table
            
            # Commit the changes to the database
            # Use cursor.commit() after inserting
            
            # Display films after insertion
            show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

            # Update a record
            # Use cursor.execute() to update a record in the film table
            
            # Commit the changes to the database
            # Use cursor.commit() after updating
            
            # Display films after update
            show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")

            # Delete a record
            # Use cursor.execute() to delete a record from the film table
            
            # Commit the changes to the database
            # Use cursor.commit() after deleting
            
            # Display films after deletion
            show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

        except mysql.connector.Error as error:
            print("Error occurred:", error)

        finally:
            # Close the cursor and the connection
            cursor.close()
            mydb.close()

# Call the main function to execute the tasks
if __name__ == "__main__":
    main()
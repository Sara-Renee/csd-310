# Sara White
# CSD-310
# Assignment 7.2


import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "Csdpass310!",
    "host": "localhost",
    "database": "movies"
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("\n-- DISPLAYING Studio RECORDS --")

    cursor.execute("SELECT studio_id, studio_name FROM studio")
    studios = cursor.fetchall()

    for studio in studios:
        print("Studio ID:", studio[0])
        print("Studio Name:", studio[1])
        print()

    print("-- DISPLAYING Genre RECORDS --")

    cursor.execute("SELECT genre_id, genre_name FROM genre")
    genres = cursor.fetchall()

    for genre in genres:
        print("Genre ID:", genre[0])
        print("Genre Name:", genre[1])
        print()

    print("-- DISPLAYING Short Film RECORDS --")

    cursor.execute("""
                   SELECT movie_name, movie_runtime FROM movies
                   WHERE movie_runtime < 120
                   """)
    short_films = cursor.fetchall()

    for film in short_films:
        print("Film Name:", film[0])
        print("Runtime:", film[1])
        print()

    print("-- DISPLAYING Director RECORDS in Order --")

    cursor.execute("""
                   SELECT movie_name, movie_director FROM movies
                   ORDER BY movie_director ASC
                   """)
    directors = cursor.fetchall()

    for film in directors:
        print("Film Name:", film[0])
        print("Director:", film[1])
        print()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

finally:
    db.close()

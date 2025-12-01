# Sara White
# CSD-310
# Assignment 8.2

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "Csdpass310!",
    "host": "localhost",
    "database": "movies"
}


def show_films(cursor, title):
    cursor.execute("""
        SELECT 
            m.movie_name AS Name, m.movie_director  AS Director, g.genre_name AS Genre,
            s.studio_name AS Studio
        FROM movies AS m
        INNER JOIN genre AS g ON m.genre_id  = g.genre_id
        INNER JOIN studio AS s ON m.studio_id = s.studio_id
        ORDER BY m.movie_name
    """)
    films = cursor.fetchall()

    print("\n-- {} --".format(title))
    for film in films:
        print("Film Name:", film[0])
        print("Director:", film[1])
        print("Genre Name:", film[2])
        print("Studio Name:", film[3])
        print()


def main():
    try:
        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        # show initial display
        show_films(cursor, "DISPLAYING FILMS")

        # insert new film 'Billy Liar'
        insert_query = """
            INSERT INTO movies
                (movie_name, movie_release_date, movie_runtime,
                 studio_id, genre_id, movie_director)
            VALUES
                (%s, %s, %s, %s, %s, %s)
        """
        insert_values = ("Billy Liar", "1963-08-15", 98, 2, 1, "John Schlesinger")
        cursor.execute(insert_query, insert_values)
        db.commit()

        show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

        # update Terminator 2 to Horror
        cursor.execute("""
            UPDATE movies SET genre_id = 4
            WHERE movie_name = 'Terminator 2: Judgement Day'
        """)
        db.commit()

        show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

        # delete Scott Pilgrim
        cursor.execute("""
            DELETE FROM movies
            WHERE movie_name = 'Scott Pilgrim vs. the World'
        """)
        db.commit()

        show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

    except mysql.connector.Error as err:
        """ on error code """
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("The supplied username or password are invalid")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("The specified database does not exist")
        else:
            print(err)

    finally:
        """ close connection """
        try:
            db.close()
        except NameError:
            pass


if __name__ == "__main__":
    main()


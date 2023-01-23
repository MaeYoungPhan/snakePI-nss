import sqlite3
import json
from models import Snake

def get_all_snakes():
    """Returns list of dictionaries stored in SNAKES variable"""
    # Open a connection to the database
    with sqlite3.connect("./snakes.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            s.id,
            s.name,
            s.owner_id,
            s.species_id,
            s.gender,
            s.color
        FROM snakes s
        """)

        # Initialize an empty list to hold all snake representations
        snakes = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an snake instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Snake class above.
            snake = Snake(row['id'], row['name'], row['owner_id'],
                            row['species_id'], row['gender'], row['color'])

            snakes.append(snake.__dict__)

    return snakes

def get_single_snake(id):
    """Returns dictionary of single snake from list stored in SNAKES or returns nothing."""
    with sqlite3.connect("./snakes.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            s.id,
            s.name,
            s.owner_id,
            s.species_id,
            s.gender,
            s.color
        FROM snakes s
        WHERE s.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an snake instance from the current row
        snake = Snake(data['id'], data['name'], data['owner_id'],
                            data['species_id'], data['gender'], data['color'])

        return snake.__dict__
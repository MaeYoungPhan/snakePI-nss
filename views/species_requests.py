import sqlite3
import json
from models import Species

def get_all_species():
    """Returns list of dictionaries stored in SPECIES variable"""
    # Open a connection to the database
    with sqlite3.connect("./snakes.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            s.id,
            s.name
        FROM species s
        """)

        # Initialize an empty list to hold all species representations
        species = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an species instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Species class above.
            specie = Species(row['id'], row['name'])

            species.append(specie.__dict__)

    return species

def get_single_species(id):
    """Returns dictionary of single species from list stored in SPECIES or returns nothing."""
    with sqlite3.connect("./snakes.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            s.id,
            s.name
        FROM species s
        WHERE s.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an species instance from the current row
        species = Species(data['id'], data['name'])

        return species.__dict__
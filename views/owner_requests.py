import sqlite3
import json
from models import Owner

def get_all_owners():
    """Returns list of dictionaries stored in OWNERS variable"""
    # Open a connection to the database
    with sqlite3.connect("./snakes.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.first_name,
            o.last_name,
            o.email
        FROM owners o
        """)

        # Initialize an empty list to hold all owner representations
        owners = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an owner instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Owner class above.
            owner = Owner(row['id'], row['first_name'], row['last_name'],
                            row['email'])

            owners.append(owner.__dict__)

    return owners

def get_single_owner(id):
    """Returns dictionary of single owner from list stored in OWNERS or returns nothing."""
    with sqlite3.connect("./snakes.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            o.id,
            o.first_name,
            o.last_name,
            o.email
        FROM owners o
        WHERE o.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an owner instance from the current row
        owner = Owner(data['id'], data['first_name'], data['last_name'],
                            data['email'])

        return owner.__dict__
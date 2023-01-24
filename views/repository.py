import sqlite3
import json
from models import Owner, Snake, Species

def all(resource):
    # Open a connection to the database
    with sqlite3.connect("./snakes.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
    
        if resource == 'species':
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

        if resource == 'owners':

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
    
        if resource == 'snakes':
        
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


def single(resource, id):
    with sqlite3.connect("./snakes.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        if resource == 'species':
            db_cursor.execute("""
            SELECT
                s.id,
                s.name
            FROM species s
            WHERE s.id = ?
            """, ( id, ))

            # Load the single result into memory
            data = db_cursor.fetchone()

            if data is None:
                return None

            # Create an species instance from the current row
            species = Species(data['id'], data['name'])

            return species.__dict__

        if resource == 'owners':

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

        if resource == 'snakes':
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
            
            if snake.species_id == 2:
                return ''

            else:
                return snake.__dict__

def get_snakes_by_species(species_id):
    """Returns a list of dict. of all snakes of X species"""
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
        FROM Snakes s
        WHERE s.species_id = ?
        """, ( species_id, ))

        snakes = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            snake = Snake(row['id'], row['name'], row['owner_id'],
                            row['species_id'], row['gender'], row['color'])

            snakes.append(snake.__dict__)

    return snakes

def create_snake(new_snake):
    """Args: snake (json string), returns new dictionary with id property added"""
    with sqlite3.connect("./snakes.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Snakes
            ( name, owner_id, species_id, gender, color )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_snake['name'], new_snake['ownerId'],
            new_snake['speciesId'], new_snake['gender'],
            new_snake['color'], ))

        id = db_cursor.lastrowid

        new_snake['id'] = id

    return new_snake

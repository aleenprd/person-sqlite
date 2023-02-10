import sqlite3

class Person:
    """A class that constructs the PERSON entity and holds personal information."""

    def __init__(
        self,
        connection: sqlite3.Connection,
        id: int = -1,
        first_name: str = "John",
        last_name: str = "Doe",
        age: int = 999,
    ) -> None:
        """Initialize a person entity."""
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        

    def __str__(self):
        """Overloaded str method for Person class."""
        return f"{{'id': {self.id}, 'first_name': '{self.first_name}', " + \
            f"'last_name': '{self.last_name}', 'age': {self.age}}}"

    def insert_person(self):
        """Insert the person object into table."""
        self.cursor.execute(
            """
            INSERT OR REPLACE INTO persons VALUES (?, ?, ?, ?) 
            """,
            (self.id, self.first_name, self.last_name, self.age),
        )
        self.connection.commit()

    def load_person(self, id: int):
        """Load a person from the table and set the values of the object."""
        self.cursor.execute(
            """
            SELECT * FROM persons WHERE id == ?
            """,
            (id,),
        )
        results = self.cursor.fetchone()
        if results:
            self.id = results[0]
            self.first_name = results[1]
            self.last_name = results[2]
            self.age = results[3]

    def delete_person(self, id: int):
        """Delete a person from the table."""
        self.cursor.execute(
            """
            DELETE FROM persons WHERE id == ?
            """,
            (id,),
        )
        self.connection.commit()
        
# Establish connection to database
connection = sqlite3.connect("mydata.db")

# We need a 'cursor' to execute SQL queries
# It is the interface to the database
cursor = connection.cursor()

p4 = Person(connection, 4, "Otto", "Octavius", 65)
print(p4)
p4.insert_person()

cursor.execute(
    """
    SELECT * FROM persons 
    """
)

# Then, we need to fetch the results
results = cursor.fetchall()
print(results)

p5 = Person(connection, 5, "Nick", "Fury", 45)
print(p5)
p5.insert_person()

cursor.execute(
    """
    SELECT * FROM persons 
    """
)

p5.delete_person(5)

cursor.execute(
    """
    SELECT * FROM persons 
    """
)

# Then, we need to fetch the results
results = cursor.fetchall()
print(results)
        
# But to really apply, we need to commit
connection.commit()

# Also, when done, we need to close the connection
connection.close()
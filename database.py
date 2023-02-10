import sqlite3

# Establish connection to database
connection = sqlite3.connect("mydata.db")

# We need a 'cursor' to execute SQL queries
# It is the interface to the database
cursor = connection.cursor()

cursor.execute(
    """DROP TABLE IF EXISTS persons"""
)

# Using cursor, we can directly execute SQL queries
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS persons (
        id PRIMARY KEY,
        first_name VARCHAR NOT NULL,
        last_name VARCHAR NOT NULL,
        age INTEGER NOT NULL,
        UNIQUE(id)
    );
    """
)

cursor.execute(
    """
    INSERT OR REPLACE INTO persons VALUES
        (1, 'Clark', 'Kent', 28),
        (2, 'Bruce', 'Wayne', 35),
        (3, 'Peter', 'Parker', 26)
    """
)

# This is how we can retrieve rows
# First, we execute the query using the cursor
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

# Rractice creating database file, creating connection and cursor object to interact with database, inserting and selecting data, creating DataFrames from SQL query, and creating SQL table from DataFrame.

# Import modules
import sqlite3
import pandas as pd


# Create connect to database and cursor object
connection = sqlite3.connect('Resources/TestDB.db')
cursor = connection.cursor()


# Creating a table and adding values
# Table and data was successfully created when running the script the first time

# cursor.execute('''CREATE TABLE users (
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         username TEXT NOT NULL,
#         created TEXT NOT NULl)''')
# cursor.execute('''INSERT INTO users VALUES (1, 'Carlos', 'los1234', '04/16/2022')''')
# add_users = [(2, 'Lesley', 'lsly01', '04/01/2022'),(3, 'Nina', 'tiny1', '04/15/2022')]
# cursor.executemany('''INSERT INTO users VALUES (?,?,?,?)''', add_users)
# connection.commit()


# Selecting and printing the data from the table created above
results = cursor.execute("SELECT * FROM users").fetchall()
print("results:\n", results)


# Conveting the SQL table to a Pandas DataFrame.
df1 = pd.read_sql_query('''SELECT * FROM users''', connection)
print("df1:\n", df1)


# Creating a dataframe from a dictionary
df2 = pd.DataFrame({'name':['Carlos', 'Lesley'], 'birthdate':['01/23/1980', '12/31/2000'], 'fav_food':['tacos', 'pasta']})
print("df2:\n", df2)


# Creating a dataframe from a list of lists of values
data = [['Andrew', '01/01/1990', 'tacos'], ['Julian', '01/01/2000', 'burgers'], ['Nina', '03/31/2010', 'chicken nuggets']]
df3 = pd.DataFrame(data, columns = ['name', 'birthday', 'fav_food'])
print("df3:\n", df3)


# Creating a table from DataFrame
df3.to_sql('users2', connection)


# # Selecting and printing the data from the table created above
results2 = cursor.execute('SELECT * FROM users2').fetchall()
print("results2\n", results2)

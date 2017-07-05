# Code Sample from the tutorial at https://learncodeshare.net/2015/07/02/update-crud-using-cx_oracle/
#  section titled "Resetting the data"
# The following resets the data for use with the update section
# For both tables:
#  Table data is removed.
#  The identity column is set to start with the id after the starting data.
#  Using the executemany function an array of starting data is inserted into the table.

import cx_Oracle
import os
connectString = os.getenv('DB_CONNECT') # The environment variable for the connect string: DB_CONNECT=user/password@database
con = cx_Oracle.connect(connectString)
cur = con.cursor()

# Delete rows
statement = 'delete from lcs_pets'
cur.execute(statement)

# Reset Identity Coulmn
statement = 'alter table lcs_pets modify id generated BY DEFAULT as identity (START WITH 8)'
cur.execute(statement)

# Delete rows
statement = 'delete from lcs_people'
cur.execute(statement)

# Reset Identity Coulmn
statement = 'alter table lcs_people modify id generated BY DEFAULT as identity (START WITH 3)'
cur.execute(statement)

# Insert default rows
rows = [(1, 'Bob', 35, 'I like dogs'), (2, 'Kim', 27, 'I like birds')]
cur.bindarraysize = 2
cur.setinputsizes(int, 20, int, 100)
cur.executemany("insert into lcs_people(id, name, age, notes) values (:1, :2, :3, :4)", rows)
con.commit()

# Insert default rows
rows = [(1, 'Duke', 1, 'dog'),
        (2, 'Pepe', 2, 'bird'),
        (3, 'Princess', 1, 'snake'),
        (4, 'Polly', 1, 'bird'),
        (5, 'Rollo', 1, 'horse'),
        (6, 'Buster', 1, 'dog'),
        (7, 'Fido', 1, 'cat')]
cur.bindarraysize = 2
cur.setinputsizes(int, 20, int, 100)
cur.executemany("insert into lcs_pets (id, name, owner, type) values (:1, :2, :3, :4)", rows)
con.commit()

cur.close()

## My MMLab project - Phase 1a | Trying to make evrything Pandas Readable (Making it into a CSV because its what i am comfortable with.)

# Import
import sqlite3
import pandas as pd

# Create file path
Completed_db_file  = './RedDB_CompleteData.sqlite'
Original_db_file   = './RedDB_Original.sqlite'
RandomTest_db_file = './sql-murder-mystery.sqlite'    #* Just to cross test my code #* An old random file I used when learning SQL (I think it's from Kaggle) 

# Create CSV folder path
CSV_folder = './Converted to CSV/'

# Create a SQL connection to our SQLite database
db = sqlite3.connect(Completed_db_file)               #! <--- Not working | >>>Output: DatabaseError: database disk image is malformed

# Create cursor
cursor = db.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# reading all table names
for table_name in tables:
    table_name = table_name[0]
    table = pd.read_sql_query("SELECT * from %s" % table_name, db)
    table.to_csv(CSV_folder + table_name + '.csv', index_label='index')

cursor.close()
db.close()


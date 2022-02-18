from decouple import config
import func

dbfunc = func.StudiKasus2

print("What do you want to do?\n")
print("1. Try Connect Database")
print("2. Create Database")
print("3. Create Table")
print("4. Load data from database")
print("5. Load CSV file")

choice = input("Your choice: ")

def tryConnDB():
    dbfunc._init_(dbfunc, 'host', '3306', 'root', config('PASSDB'))
    dbfunc.check_conn(dbfunc)
    dbfunc.connect_db(dbfunc)

if choice == "1":
    tryConnDB();

elif choice == "2":
    tryConnDB();
    dbname = input("Input your new database name: ")
    dbfunc.create_db(dbfunc, dbname)

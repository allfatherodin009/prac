import mysql.connector
import getpass

# Establishing the connection
mydb = mysql.connector.connect(
    host="127.0.0.1",         # Replace with your MySQL host (e.g., 'localhost')
    user="root",     # Replace with your MySQL username
    password="!JikeNe009", # Replace with your MySQL password
    database="lmsys"  # Replace with the name of your database
)
mycursor = mydb.cursor()


def logo():
        print("                 ██╗░░░░░███╗░░░███╗░██████╗  ░█████╗░░█████╗░███╗░░██╗░██████╗░█████╗░██╗░░░░░███████╗")
        print("                 ██║░░░░░████╗░████║██╔════╝  ██╔══██╗██╔══██╗████╗░██║██╔════╝██╔══██╗██║░░░░░██╔════╝")
        print("                 ██║░░░░░██╔████╔██║╚█████╗░  ██║░░╚═╝██║░░██║██╔██╗██║╚█████╗░██║░░██║██║░░░░░█████╗░░")
        print("                 ██║░░░░░██║╚██╔╝██║░╚═══██╗  ██║░░██╗██║░░██║██║╚████║░╚═══██╗██║░░██║██║░░░░░██╔══╝░░")
        print("                 ███████╗██║░╚═╝░██║██████╔╝  ╚█████╔╝╚█████╔╝██║░╚███║██████╔╝╚█████╔╝███████╗███████╗")
        print("                 ╚══════╝╚═╝░░░░░╚═╝╚═════╝░  ░╚════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░░╚════╝░╚══════╝╚══════╝")

def add_book():

    book = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    pages = input ("Enter Total Pages: ")
    price = input ("Enter Book Price: ")

    
    sqlFormula = "INSERT INTO books (book, author, pages, price) VALUES (%s, %s, %s, %s)"
    book1 = (book, author, pages, price)

    try:
        # Executing the add query
        mycursor.execute(sqlFormula, book1)
        mydb.commit()
        print(f"Rows affected: {mycursor.rowcount}")
    except mysql.connector.Error as error:
        print(f"Error: {error}")


def update_book():

    ogbook = input("Enter Original Book Name: ")
    book = input("Enter new Book Name: ")
    author = input("Enter new Author Name: ")
    pages = input ("Enter new Total Pages: ")
    price = input ("Enter new Book Price: ")

    
    sqlFormula = " UPDATE books SET book = %s, author = %s, pages = %s, price = %s WHERE book = %s; "
    
    updatebook = (book, author, pages, price, ogbook)
    
    try:
        # Executing the update query
        mycursor.execute(sqlFormula, updatebook)
        mydb.commit()
        print(f"Rows affected: {mycursor.rowcount}")
    except mysql.connector.Error as error:
        print(f"Error: {error}")



def search_book():
    
    search = input("Enter Name of book to be searched: ")

    sqlFormula = " SELECT id, book, author, pages, price FROM books WHERE book = %s;"

    try:
        # Executing the update query
        mycursor.execute(sqlFormula, (search,))
        results = mycursor.fetchall()
        if results:
            for row in results:
                print(f"ID: {row[0]}, Book: {row[1]}, Author: {row[2]}, Pages: {row[3]}, Price: {row[4]}")
        else:
            print("No Book found with that name!")
        
    except mysql.connector.Error as error:
        print(f"Error: {error}")

    
def delete_book():
    
    delete1 = input("Enter the name of the book to delete: ")

    
    sqlFormula = "DELETE FROM books WHERE book = %s;"

    try:
        mycursor.execute(sqlFormula, (delete1,))
        mydb.commit()
        
        print(f"Rows affected: {mycursor.rowcount}")
    except mysql.connector.Error as error:
        print(f"Error: {error}")


    


def show_allbooks():

    sqlFormula = "SELECT * FROM books;"

    try:
        mycursor.execute(sqlFormula)
        results = mycursor.fetchall()
        for row in results:
            print(f"ID: {row[0]} , Book: {row[1]} , Author: {row[2]} , Pages: {row[3]} , Price: {row[4]}")

    except mysql.connector.Error as error:
        print(f"Error: {error}")



def command():
    while(True):
        
        a = input("LMSConsole>>> ")

        if a == "--addbook":
            
            add_book()
            print("Info added")

        elif a == "--searchbook":
            search_book()

        elif a == "--updatebook":
            update_book()
            

        elif a == "--deletebook":
            delete_book()

        elif a == "--showallbooks":
            show_allbooks()

        elif a == "--exit":
            exit()

        else:
            print("Invalid Command!")








def login():
    passwd = "achilles"
    username = "achilles"
    user = input("Enter Username: ")
    password = getpass.getpass("Enter Password: ")
    if user == username :
        if password == passwd :
            command()

    else:
        print("Invalid Username or Password!")


logo()
login()







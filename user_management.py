import sqlite3
from catalog_management import *


def add_user(name, password, email, role):
    #Database connection stablish 
    conn = sqlite3.connect('library_management.db')
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO users (name, password, email, role) VALUES (?, ?, ?, ?)', (name, password, email, role))
        conn.commit()
        #user ID
        last_id = cursor.lastrowid
        print(f"User '{name}' added successfully with ID {last_id}!")

    except sqlite3.IntegrityError:
        print(f"Error: A user with email '{email}' already exists.")
    #Database connection close
    conn.close()


def user_authenticate(usr_id, usr_password):
    #Database connection stablish 
    conn = sqlite3.connect('library_management.db')
    cursor = conn.cursor()

    status = False
    password = cursor.execute('SELECT password FROM users WHERE user_id=?', (usr_id,)).fetchone()

    #print(f'******{password[0]}*********')

    try:
        if usr_password == password[0]:
            status = True
    except:
        pass
    
    #Database connection close
    conn.close()
        
    return status


def add_librarian(name, password, email, role):
    #Database connection stablish 
    conn = sqlite3.connect('library_management.db')
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO librarians (name, password, email, role) VALUES (?, ?, ?, ?)', (name, password, email, role))
        
        lib_id = cursor.lastrowid
        
        conn.commit()
        #user ID
        print(f"User '{name}' added successfully with ID {lib_id}!")

    except sqlite3.IntegrityError:
        print(f"Error: A user with email '{email}' already exists.")
    #Database connection close
    conn.close()


def librarian_authenticate(lib_id, lib_password):
    #Database connection stablish 
    conn = sqlite3.connect('library_management.db')
    cursor = conn.cursor()

    status = False
    password = cursor.execute('SELECT password FROM librarians WHERE librarian_id=?', (lib_id,)).fetchone()
    try:
        if lib_password == password[0]:
            status = True
    except:
        pass
    
    #Database connection close
    conn.close()
        
    return status


#User options
def usr_options():
    wrong_option = 5

    while True:
        if wrong_option <= 0:
            break
        print('------------------------------------------')
        print('|              Student Menu              |')
        print('------------------------------------------')
        print('|             1. View Books              |')
        print('|             2. Borrow Books            |')
        print('|             3. Return Books            |')
        print('|             4. Search Books            |')
        print('------------------------------------------')

        print('Press enter to exit')
        print('Enter your option ')
        choice = input('---> ')

        if len(choice) == 0:
            break

        match choice:
            case '1':
                view_books()

            case '2':
                book_id = input("Enter Book ID of the book\n--->")
                borrow_book(book_id)
            
            case '3':
                book_id = input("Enter Book ID of the book\n--->")
                return_book(book_id)
            
            case '4':
                search_book = input("Enter for Search\n--->")
                search_books(search_book)
            
            case _:
                print('------------------------------------------')
                print('|       Enter the mentioned choices      |')
                print(f'|       Remaining attempts : {wrong_option}           |')
                print('------------------------------------------')
                wrong_option -= 1


#Librarian Options
def lib_options():
    wrong_option = 5

    while True:
        if wrong_option <= 0:
            break
        print('------------------------------------------')
        print('|              Librarian Menu            |')
        print('------------------------------------------')
        print('|             1. View Books              |')
        print('|             2. Add Books               |')
        print('|             3. Update Books            |')
        print('|             4. Remove Books            |')
        print('------------------------------------------')
        print('Press enter to exit')
        print('Enter your option ')
        choice = input('---> ')

        if len(choice) == 0:
            break

        match choice:
            case '1':
                view_books()
            case '2':
                isbn = input("Enter ISBN of the book\n--->").lower()
                title = input("Enter Title of the book\n--->").lower()
                author = input("Enter Author of the book\n--->").lower()
                genre = input("Enter Genre of the book\n--->")
                total_copies = int(input("Enter Total Copies of the book\n--->"))
                
                add_book(isbn, title, author, genre, total_copies)

            case '3':
                book_id = input("Enter Book ID of the book\n--->")
                book_count = int(input("Enter the Book count\n--->"))

                update_book(book_id, book_count)

            case '4':
                book_id = input("Enter Book ID to remove\n--->")
                remove_book(book_id)
            case _:
                print('------------------------------------------')
                print('|       Enter the mentioned choices      |')
                print(f'|       Remaining attempts : {wrong_option}           |')
                print('------------------------------------------')
                wrong_option -= 1



#import libraries
import sqlite3



# Catalog Management Functions for Users

def view_books():
    #Database connection stablish 
    conn = sqlite3.connect('library_management.db')
    cursor = conn.cursor()

    books = cursor.execute('SELECT * FROM books').fetchall()
    if books:
        print("\nCatalog of Books:")
        print("-" * 80)
        print(f"{'ID':<5}{'ISBN':<15}{'Title':<25}{'Author':<20}{'Genre':<15}{'Total':<7}{'Available':<10}")
        print("-" * 80)
        for book in books:
            print(f"{book[0]:<5}{book[1]:<15}{book[2]:<25}{book[3]:<20}{book[4]:<15}{book[5]:<7}{book[6]:<10}")
    else:
        print("No books found in the catalog.")
    
    #Database connection close
    conn.close()


def borrow_book(book_id):
    #Database connection stablish 
    conn = sqlite3.connect('library_management.db')
    cursor = conn.cursor()

    avl_books = cursor.execute('SELECT available_copies FROM books WHERE book_id=?', (book_id,)).fetchone()
    if avl_books is None:
        print(f"No book found with ID {book_id}")
        return
    elif avl_books[0] == 0:
        print("No Available copies")
        return

    print("availabel books:", avl_books[0])
    
    new_avl_books = avl_books[0] - 1

    try:
        cursor.execute(f'''UPDATE books 
                        SET available_copies = ?
                        WHERE book_id = ?''', (new_avl_books, book_id))
        conn.commit()
        print(f"Book with ID {book_id} Borrowed successfully!")
    except Exception as e:
        print(e)
    
    #Database connection close
    conn.close()


def return_book(book_id):
    #Database connection stablish 
    conn = sqlite3.connect('library_management.db')
    cursor = conn.cursor()

    avl_books = cursor.execute('SELECT available_copies, total_copies FROM books WHERE book_id=?', (book_id,)).fetchone()
    if avl_books is None:
        print(f"No book found with ID {book_id}")
        return
    elif avl_books[0] == avl_books[1]:
        print("No books issued to anyone")
        return
    
    print("availabel books:", avl_books[0])
    
    new_avl_books = avl_books[0] + 1

    try:
        cursor.execute(f'''UPDATE books 
                        SET available_copies = ?
                        WHERE book_id = ?''', (new_avl_books, book_id))
        conn.commit()
        print(f"Book with ID {book_id} Returned successfully!")
    except Exception as e:
        print(e) 

    #Database connection close
    conn.close()       


def search_books(search_term):
    #Database connection stablish 
    conn = sqlite3.connect('library_management.db')
    cursor = conn.cursor()

    books = cursor.execute("SELECT * FROM books WHERE book_id=? OR isbn=? OR title LIKE ? OR author LIKE ? OR genre LIKE ?",
                           (search_term, search_term, f'%{search_term}%', f'%{search_term}%', f'%{search_term}%')).fetchall()
    if books:
        print("\nSearch Results:")
        print("-" * 80)
        print(f"{'ID':<5}{'ISBN':<15}{'Title':<25}{'Author':<20}{'Genre':<15}{'Total':<7}{'Available':<10}")
        print("-" * 80)
        for book in books:
            print(f"{book[0]:<5}{book[1]:<15}{book[2]:<25}{book[3]:<20}{book[4]:<15}{book[5]:<7}{book[6]:<10}")
    else:
        print(f"No books found matching '{search_term}'.")

    #Database connection close
    conn.close()


# Catalog Management Functions for Librarian
def add_book(isbn, title, author, genre, total_copies=1):
    #Database connection stablish 
    conn = sqlite3.connect('library_management.db')
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO books (isbn, title, author, genre, total_copies, available_copies) VALUES (?, ?, ?, ?, ?, ?)',
                       (isbn, title, author, genre, total_copies, total_copies))

        # Initialize inventory for the book
        book_id = cursor.lastrowid

        conn.commit()
        print(f"Book '{title}' added successfully with ID {book_id}!")
    except sqlite3.IntegrityError:
        print(f"Error: A book with ISBN '{isbn}' already exists.")
    
    #Database connection close
    conn.close()


def remove_book(book_id):
    #Database connection stablish 
    conn = sqlite3.connect('library_management.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM books WHERE book_id=?', (book_id,))
    #cursor.execute('DELETE FROM inventory WHERE book_id=?', (book_id,))
    conn.commit()
    print(f"Book with ID {book_id} deleted successfully!")

    #Database connection close
    conn.close()


def update_book(book_id, book_count=0):
    #Database connection stablish 
    conn = sqlite3.connect('library_management.db')
    cursor = conn.cursor()

    curr_count = cursor.execute('SELECT total_copies, available_copies FROM books WHERE book_id=?', (book_id,)).fetchone()
    if not curr_count:
        print(f"No book found with ID {book_id}")
        return

    # Calculate the new available copies based on the change in total copies
    new_total_copies = curr_count[0] + book_count
    new_available_copies = curr_count[1] + book_count

    if new_available_copies < 0:
        print("Error: Cannot reduce total copies below the number of currently issued copies.")
        return

    try:
        cursor.execute('''UPDATE books 
                  SET total_copies = ?, available_copies = ? 
                  WHERE book_id = ?''', (new_total_copies, new_available_copies, book_id))


        conn.commit()
        print(f"Book with ID {book_id} updated successfully!")
    except sqlite3.IntegrityError:
        print(f"Error: A book with ISBN '{new_isbn}' already exists.")

    #Database connection close
    conn.close()



import sqlite3

# Connect to the SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('library_management.db')
cursor = conn.cursor()

def create_tables():
    # Create users table (assuming user management is handled separately)
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        password TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        role TEXT NOT NULL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS librarians (
                        librarian_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        password TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        role TEXT DEFAULT "Librarian"
                    )''')

    # Create books table for Catalog Management
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        isbn TEXT UNIQUE NOT NULL,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        genre TEXT,
                        total_copies INTEGER DEFAULT 1,
                        available_copies INTEGER DEFAULT 1
                    )''')

create_tables()


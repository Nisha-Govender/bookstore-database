#----------------------------- Part 2 -----------------------------



# import SQLITE module

import sqlite3



# create file

db = sqlite3.connect('ebookstore_db')



# create book table

cursor = db.cursor()



#----------------------------- Part 2 -----------------------------



# 

def populate_db(cursor):

    cursor.execute('''CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, qty INTEGER)''')



    cursor.execute('''INSERT INTO books(id,Title,Author,Qty)VALUES(?,?,?,?)''',

                   (3001, "A Tale of Two Cities", "Charles Dickens", 30))



    cursor.execute('''INSERT INTO books(id,Title,Author,Qty)VALUES(?,?,?,?)''',

                   (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40))



    cursor.execute('''INSERT INTO books(id,Title,Author,Qty)VALUES(?,?,?,?)''',

                   (3003, "The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25))



    cursor.execute('''INSERT INTO books(id,Title,Author,Qty)VALUES(?,?,?,?)''',

                   (3004, "The Lord of The Rings", "J.R.R Tolkien", 37))



    cursor.execute('''INSERT INTO books(id,Title,Author,Qty)VALUES(?,?,?,?)''',

                   (3005, "Alice in Wonderland", "Lewis Carrol", 12))



    db.commit()



# view all books in the database

def view_table(db_cursor):

    print('                                          INVENTORY                                             ')

    print('{:<20}{:<50}{:<20}{}'.format("ID", "Title", "Author", "Quantity"))

    for row in db_cursor:

        print('{:<20}{:<50}{:<20}{}'.format(row[0], row[1], row[2], row[3]))

    print("\n")



# add book to database

def add_book(cursor):

    book_id = input("Please enter book ID: ")

    book_title = input("Please enter book Title: ")

    book_author = input("Please enter book Author: ")

    book_quantity = input("Please enter book quantity: ")



    cursor.execute('''INSERT INTO BOOKS(id,Title,Author,Qty) VALUES(?,?,?,?)''',

                   (book_id, book_title, book_author, book_quantity))

    db.commit()



    print("Book Added!")

    cursor.execute('''SELECT*FROM books''')

    view_table(cursor)

 

# update book in database

def update_book(cursor):



    book_ID = input("Enter Book ID to Update avaiable quantity: ")

    cursor.execute('''SELECT*FROM books WHERE id=?''', (book_ID,))

    book_found = cursor.arraysize == 1



    if book_found : 

        view_table(cursor)

        book_QTY = input("Enter new book quantity: ")

        cursor.execute('''UPDATE books set Qty =? WHERE id =?''', (book_QTY, book_ID))

        print("Book Quantity updated.\n")

        cursor.execute('''SELECT*FROM books''')

        view_table(cursor)



    else: 

        print("Book does not exist!")



# delete book from database

def delete_book(cursor):

    cursor.execute('''SELECT*FROM books''')

    book_id = int(input("Enter book ID to delete: "))

    book_found = False



    for i in cursor:

        if i[0] == book_id:

            cursor.execute('''DELETE FROM books WHERE id = ?''', (book_id,))

            db.commit()

            print("Book Deleted!")

            cursor.execute('''SELECT*FROM books''')

            view_table(cursor)

            book_found = True

            break



    if not book_found:

        print("Book does not exist!")



# search book by title

def search_book(cursor):   

    book_title = input("Enter Book Title to search: ") +'%'

    cursor.execute('''SELECT*FROM books WHERE title LIKE '%{}%' '''.format(book_title))



    view_table(cursor)





#----------------------------- Part 3 -----------------------------

    

# Popluate db with init data 

populate_db(cursor)



# user input menu

print("\n1. Add Book\n2. Update Book\n3. Delete Book\n4. Search Book\n0. Exit")

user_input = input("Please Enter your option: ")



while user_input != "0":

    if user_input == "1":

            add_book(cursor)

    elif user_input == "2":

            update_book(cursor)

    elif user_input == "3":

            delete_book(cursor)

    elif user_input == "4":

            search_book(cursor)



    print("1. Add Book\n2. Update Book\n3. Delete Book\n4. Search Book\n0. Exit")

    user_input = input("Please Enter your option: ")





if user_input != "0": 

    print("Program Terminated!")

    db.close()




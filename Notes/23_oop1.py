'''
                            Object Oriented Programming
What are objects?   Can you name a few objects around you
Book, Laptop, Phone, Clock, Charger

A book is a general class objects
How to change this generality to specificity

Name: Harry Potter & Philosopher's Stone
Author: JK Rowling
Genre: Fiction
NumPages: 250
Publication: Bloomsbury

The above list contains ATTRIBUTES of the class BOOK
Harry Potter & Philosopher's Stone is an OBJECT of the CLASS Book

Lets translate to code
'''

class Book:
    # constructor - define all attributes here
    def __init__(self, name, author, pages):
        self.bookName = name
        self.authorName = author
        self.numPages = pages

'NOW LETS ACTUALLY CREATE AN OBJECT OF THIS CLASS'
book1 = Book("Harry Potter", "JK", 250)
'''
                                    book1
self.bookName = "Harry Potter"
self.authorName = "JK"
self.numPages = 250

'''
book2 = Book("LOTR", "Tolkien", 800)
'''
                                    book2
self.bookName = "LOTR"
self.authorName = "Tolkien"
self.numPages = 800

'''

print(book1.authorName)
print(book2.numPages)
# OVERWRITING ATTRIBUTES IS POSSIBLE
book1.authorName = "Muqtaza"
print(book1.authorName)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def displayDetails(self):
        print(f"The book {self.title} is written by {self.author}")

class audioBook(Book):
    def __init__(self, title, author, narrator):
        super().__init__(title, author)
        self.narrator = narrator

    def displayAudioDetails(self):
        super().displayDetails()    #CALL A FUNCTION FROM PARENT CLASS WITHIN A CHILD CLASS
        print(f"The book is read by {self.narrator}")

LOTR = audioBook("LOTR", "Tolkien", 'Robert Inglis')

LOTR.displayAudioDetails()
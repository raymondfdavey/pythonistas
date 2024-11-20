class Borrower:
    """Represents a person who can borrow books."""

    new_id_code = 1  # Class variable

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.id = Borrower.new_id_code
        Borrower.new_id_code += 1  # Updates for next new borrower...
        self.books_borrowed = []

    def borrowBook(self, book):
        self.books_borrowed.append(book)
    
    def showAllBooks(self):
        print(f"books currently borrowed by {self.firstname} {self.lastname}:")
        for book in self.books_borrowed:
            print(f"{book.title}")
            
    def showBorrowerDetails(self):
        print(f"name: {self.firstname} {self.lastname}")
        print(f"{self.id=}")

class Book:
    """A class to represent a book in a library."""
    def __init__(self, title, author, code):
        self.title=title
        self.author=author
        self.code=code
        self.onLoan=False
        
    # Add code here...
    def showtitle(self):
        print(self.title)

class Library:
    """A class to represent a lending library."""
    # Add code here...
    def __init__(self):
         self.allBorrowers = []
         self.allBooks = []
         
    def addBook(self, book):
        self.allBooks.append(book)
        
    def addBorrower(self, borrower):
        self.allBorrowers.append(borrower)
    
    def lendBook(self, borrower, book):
        print(f"lenfing {book.title} to {borrower.firstname} {borrower.lastname}")
        if book.onLoan:
            print(f"cannot loan {book.title}, it is already on loan")
        else:
            borrower.borrowBook(book)
            book.onLoan=True


def main():
    # Create some books...
    book1 = Book('Kafkas Motorbike', 'Bridget Jones', 1290)
    book2 = Book('Cooking with Custard', 'Jello Biafra', 1002)
    book3 = Book('History of Bagpipes', 'John Cairncross', 987)

    # Put the books in the library
    library = Library()  # Creates the library
    library.addBook(book1)
    library.addBook(book2)
    library.addBook(book3)

    # Create some borrowers...
    bor1 = Borrower('Kevin', 'Wilson')
    bor2 = Borrower('Rita', 'Shapiro')
    bor3 = Borrower('Max', 'Normal')

    library.addBorrower(bor1)
    library.addBorrower(bor2)
    library.addBorrower(bor3)

    # Make some loans...
    library.lendBook(bor1, book1)
    bor1.showBorrowerDetails()
    bor1.showAllBooks()
    library.lendBook(bor2, book3)
    bor2.showBorrowerDetails()
    bor2.showAllBooks()
    # Try to lend book3 out again...
    library.lendBook(bor3, book3)

if __name__ == "__main__":
    main()

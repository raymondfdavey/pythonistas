class Borrower:
    """Represents a person who can borrow books."""

    new_id_code = 1  # Class variable

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.id = Borrower.new_id_code
        Borrower.new_id_code += 1  # Updates for next new borrower...
        self.books_borrowed = []

    def borrow_book(self, book):
        self.books_borrowed.append(book)

    def show_all_books(self):
        if len(self.books_borrowed) == 0:
            print('No books are out at the moment.')
        else:
            for b in self.books_borrowed:
                b.show_title()

    def show_borrower_details(self):
        print(f'{self.firstname} {self.lastname}, id: {self.id}')

class Book:
    """A class to represent a book in a library."""

    def __init__(self, title, author, code):
        self.title = title
        self.author = author
        self.code = code
        self.on_loan = False

    def show_title(self):
        print(f'Title: {self.title}')

class Library:
    """A class to represent a lending library."""

    def __init__(self):
        self.all_borrowers = []
        self.all_books = []

    def add_book(self, book):
        self.all_books.append(book)

    def add_borrower(self, borrower):
        self.all_borrowers.append(borrower)

    def lend_book(self, borrower, book):
        if not book.on_loan:
            print(f'Lending book {book.title} to {borrower.firstname} {borrower.lastname}')
            book.on_loan = True
            borrower.borrow_book(book)
        else:
            print("Sorry that's already on loan.")

def main():
    # Create some books...
    book1 = Book('Kafkas Motorbike', 'Bridget Jones', 1290)
    book2 = Book('Cooking with Custard', 'Jello Biafra', 1002)
    book3 = Book('History of Bagpipes', 'John Cairncross', 987)

    # Put the books in the library
    library = Library()  # Creates the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Create some borrowers...
    bor1 = Borrower('Kevin', 'Wilson')
    bor2 = Borrower('Rita', 'Shapiro')
    bor3 = Borrower('Max', 'Normal')

    library.add_borrower(bor1)
    library.add_borrower(bor2)
    library.add_borrower(bor3)

    # Make some loans...
    library.lend_book(bor1, book1)
    bor1.show_borrower_details()
    bor1.show_all_books()
    library.lend_book(bor2, book3)
    bor2.show_borrower_details()
    bor2.show_all_books()
    # Try to lend book3 out again...
    library.lend_book(bor3, book3)

if __name__ == "__main__":
    main()

class Library:
    def __init__(self, filename='books.txt'):
        self.filename = filename

    def listBooks(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.read().splitlines()
                for line in lines:
                    book = line.split(',')
                    bookName = book[0]
                    author = book[1]
                    print(f'Book: {bookName}, Author: {author}')
        except FileNotFoundError:
            print("The library is empty or the file doesn't exist.")

    def addBook(self):
        name = input("Enter the book title: ")
        author = input("Enter the author: ")
        releaseDate = input("Enter the first release year: ")
        numberOfPages = input("Enter the number of pages: ")
        book = f'{name},{author},{releaseDate},{numberOfPages},{numberOfPages}\n'
        try:
            with open(self.filename, 'a') as file:
                file.write(book)
            print('Book added to the library.')
        except IOError:
            print("Could not write to file.")

    def removeBook(self):
        rmBook = input('Enter the book name which you want to remove: ')
        found = False
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
            with open(self.filename, 'w') as file:
                for line in lines:
                    book = line.split(',')
                    bookName = book[0]
                    if bookName.strip() == rmBook.strip():
                        found = True
                    else:
                        file.write(line)
            if found:
                print(f"The book '{rmBook}' has been removed from the library.")
            else:
                print(f"The book '{rmBook}' was not found in the library.")
        except FileNotFoundError:
            print("The library is empty or the file doesn't exist.")
        except IOError:
            print("Error occurred while accessing the file.")


library = Library()
options = int(input(' 1 to list books,\n 2 to add a book,\n 3 to remove a book: '))
if(options == 1 ):
    library.listBooks()
    print('--------------------')
elif(options == 2 ):
    library.addBook()
    print('--------------------')
elif(options == 3 ):
    library.removeBook() 
    print('--------------------')
    



        
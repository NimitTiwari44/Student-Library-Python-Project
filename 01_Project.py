class Library:
    def __init__(self, listOfBooks , numberOfBooks):
        self.books = listOfBooks
        self.number = numberOfBooks
    
    def displayAvailableBooks(self):
        print(f"{self.number} Books present in the library : ")
        for books in self.books:
            print(" * " + books)
            
    def borrowBooks(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. You have to return it back within 30 DAYS ")
            self.books.remove(bookName)
            return True
        else:
            print(f"Sorry, This {bookName} book is not available currently ")
            return False

    def returnBooks(self, bookName):
        self.books.append(bookName)
        print(f"You have returned {bookName} book ")

            

class Student:
        
    def requestBooks(self):
        self.book = input("Enter the name of the book you want to borrow :")
        a = str(self.book).capitalize()
        return a
        
    
    def returnBooks(self):
        self.book = input("Enter the name of the book you want to return :")
        a = str(self.book).capitalize()
        return a
        
    
if __name__ == "__main__":
    centraLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"], 4)  
    
    student = Student()

    while(True):
        welcomeMsg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        
        print(welcomeMsg)
    
        c = int(input("Enter your choice : \n"))
        if c == 1:
            centraLibrary.displayAvailableBooks()
        elif c == 2 :
            centraLibrary.borrowBooks(student.requestBooks())
        elif c == 3 :
            centraLibrary.returnBooks(student.returnBooks())
        elif c == 4 :
            exit()
        else:
            print("Invalid choice")


       
    
        

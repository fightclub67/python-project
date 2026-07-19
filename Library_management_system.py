while True:
    print("\nA) Add book")
    print("\nB) View books")
    print("\nC) Search book")
    print("\nD) Borrow book")
    print("\nE) Return book")
    print("\nF) Delete book")
    print("\nG) Exit")
    choice = input("choose an option: ")
    if choice == "A":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        with open("books.txt", "a") as file:
            file.write(f"{title} | {author} | Available\n")
    elif choice == "B":
        with open("books.txt", "r") as file:
            books = file.read()
            if not books:
                print("No books found!")
            else:
                print(books)
    elif choice == "C":
        search_title = input("Enter book title: ")
        with open("books.txt", "r") as file:
            books = file.read()
            if search_title in books:
                print(search_title)
            else:
                print("Book Not found!")
    elif choice == "D":
        borrow_title = input("Enter book title: ")
        with open("books.txt", "r") as file:
            books = file.read().splitlines()
            for i in range(len(books)):
                if borrow_title in books[i]:
                    if "Available" in books[i]:
                        books[i] = books[i].replace("Available", "Borrowed")
                        with open("books.txt", "w") as file:
                            for book in books:
                                file.write(book + "\n")
    elif choice == "E":
        return_title = input("Enter book title: ")
        with open("books.txt", "r") as file:
            books = file.read().splitlines()
            for i in range(len(books)):
                if return_title in books[i]:
                    if "Borrowed" in books[i]:
                        books[i] = books[i].replace("Borrowed", "Available")
                        with open("books.txt", "w") as file:
                            for book in books:
                                file.write(book + "\n")
    elif choice == "F":
        delete_title = input("Enter book title to delete: ")
        with open("books.txt", "r") as file:
            books = file.read().splitlines()
            new_books = []
            for book in books:
                if delete_title not in book:
                    new_books.append(book)
            with open("books.txt", "w") as file:
                for new_book in new_books:
                    file.write(new_book + "\n")
                    print("Book deleted!")
    elif choice == "G":
        print("Goodbye!")
        break
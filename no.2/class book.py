class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def get_description(self):
        return f"{self.title} by {self.author}, published in {self.year_published}"

def sort_books_by_year(book_list):
    """
    Takes a list of Book objects and returns a sorted list based on the year published.
    Handles empty lists and documents any errors.
    """
    try:
        return sorted(book_list, key=lambda x: x.year_published)
    except Exception as e:
        print(f"Error sorting books: {e}")
        return []

# Instantiate two Book objects
book1 = Book("Think and grow rich", "Napoleon HILS", 1925)
book2 = Book("How to eat food in  town", "sekitto Abdul", 2000)
book3 = Book("rich dad poor dad", "robert kiyosaki", 2005)
book4 = Book("How to parsued her", "Nakacwa Brenda", 2019)
book5 = Book("Words of wisdom","Tuhame Thomas", 2020)

# Display the descriptions of the books
print(book1.get_description())
print(book2.get_description())
print(book3.get_description())
print(book4.get_description())
print(book5.get_description())

# Part B: Iteration Techniques

# Iterate through a sorted list of books
sorted_books = sort_books_by_year([book1, book2,book3,book4,book5])
print("\nBooks sorted by year published:")

print('\n BOOKS SORTED FOR LOOP')
# Using a for loop
for book in sorted_books:
    print(f"Title: {book.title}    , Author:    {book.author}, Year Published: {book.year_published}")

# Using a while loop
print('\n BOOKS SORTED USING WHILE LOOP')
i = 0
while i < len(sorted_books):
    book = sorted_books[i]
    print(f"Title: {book.title}, Author: {book.author}, Year Published: {book.year_published}")
    i += 1

# Advanced Looping: Search for a book by title
while True:
    search_title = input("\nEnter a book title to search (or 'q' to quit): ")
    if search_title.lower() == 'q':
        break

    found = False
    for book in sorted_books:
        if book.title.lower() == search_title.lower():
            print(f"Found: {book.get_description()}")
            found = True
            break

    if not found:
        print(f"Sorry, '{search_title}' was not found in the list.")

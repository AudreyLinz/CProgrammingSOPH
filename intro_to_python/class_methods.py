
class Book:
    total_book = 0  # class variable to count all books

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        Book.total_book += 1  # correct class variable name

    @classmethod
    def reset_total_books(cls):
        """Reset the total number of books to zero"""
        cls.total_book = 0

    @classmethod
    def from_dict(cls, data: dict):
        # Create a Book instance from a dictionary
        return cls(data["title"], data["author"], data["year"])

    def __str__(self):
        # Nicely format the book object when printed
        return f"{self.title} by {self.author} ({self.year})"

# Usage:
book1 = Book("Python 101", "Jonny", 2023)
data = {"title": "Learn Py", "author": "Deadman", "year": 2020}
book2 = Book.from_dict(data)

print(book1)
print(book2)
print("Total books:", Book.total_book)

class Book:
  """
  Represents a book in the library.
  """

  def __init__(self, title, author):
    """
    Initializes a Book object with a title, author, and availability status.

    Args:
      title (str): The title of the book.
      author (str): The author of the book.
    """
    self.title = title
    self.author = author
    self._is_checked_out = False  # Private attribute to track availability

  def check_out(self):
    """
    Marks the book as checked out, making it unavailable.
    """
    self._is_checked_out = True

  def return_book(self):
    """
    Marks the book as returned, making it available.
    """
    self._is_checked_out = False

  def is_available(self):
    """
    Returns True if the book is available, False otherwise.
    """
    return not self._is_checked_out

class Library:
  """
  Represents a library that manages a collection of books.
  """

  def __init__(self):
    """
    Initializes a Library object with an empty list of books.
    """
    self._books = []

  def add_book(self, book):
    """
    Adds a book to the library's collection.

    Args:
      book (Book): The book object to add.
    """
    self._books.append(book)

  def check_out_book(self, title):
    """
    Attempts to check out a book by title, marking it unavailable if found.

    Args:
      title (str): The title of the book to check out.

    Returns:
      bool: True if the book was checked out successfully, False otherwise.
    """
    for book in self._books:
      if book.title == title and book.is_available():
        book.check_out()
        return True
    return False

  def return_book(self, title):
    """
    Attempts to return a book by title, marking it available if found.

    Args:
      title (str): The title of the book to return.

    Returns:
      bool: True if the book was returned successfully, False otherwise.
    """
    for book in self._books:
      if book.title == title:
        book.return_book()
        return True
    return False

  def list_available_books(self):
    """
    Prints a list of all available books in the library.
    """
    print("Available books:")
    for book in self._books:
      if book.is_available():
        print(f"- {book.title} by {book.author}")

# Example usage (uncomment for testing)
# library = Library()
# library.add_book(Book("Brave New World", "Aldous Huxley"))
# library.add_book(Book("1984", "George Orwell"))
# library.list_available_books()
# library.check_out_book("1984")
# library.list_available_books()
# library.return_book("1984")
# library.list_available_books()

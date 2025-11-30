# library_management.py

class Book:
    """
    Represents a book with a public title and author and a private
    _is_checked_out flag to track availability.
    """
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self) -> bool:
        """Mark the book as checked out. Return True if successful, False if already checked out."""
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_back(self) -> bool:
        """Return the book (make it available). Return True if successful, False if it wasn't checked out."""
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self) -> bool:
        """Return True if the book is available for checkout."""
        return not self._is_checked_out

    def __str__(self) -> str:
        """User-friendly string representation."""
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a private list of Book instances.
    Methods:
      - add_book(book)
      - check_out_book(title)
      - return_book(title)
      - list_available_books()
    """
    def __init__(self):
        self._books = []

    def add_book(self, book: Book) -> None:
        """Add a Book instance to the library collection."""
        if not isinstance(book, Book):
            raise TypeError("add_book expects a Book instance.")
        self._books.append(book)

    def _find_book_by_title(self, title: str):
        """Internal helper: return the Book instance with matching title, or None."""
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title: str) -> bool:
        """
        Attempt to check out a book by title.
        Returns True if checkout succeeded, False otherwise (not found or already checked out).
        """
        book = self._find_book_by_title(title)
        if book is None:
            return False
        return book.check_out()

    def return_book(self, title: str) -> bool:
        """
        Attempt to return a book by title.
        Returns True if return succeeded, False otherwise (not found or wasn't checked out).
        """
        book = self._find_book_by_title(title)
        if book is None:
            return False
        return book.return_back()

    def list_available_books(self) -> None:
        """Print all books that are currently available (not checked out)."""
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No available books.")
            return
        for book in available:
            print(str(book))
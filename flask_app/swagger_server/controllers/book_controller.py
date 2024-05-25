import connexion
import six

from swagger_server.models.book import Book  # noqa: E501
from swagger_server import util


def add_book(body):  # noqa: E501
    """Add a new book

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Book.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_book(book_id):  # noqa: E501
    """Delete a book

     # noqa: E501

    :param book_id: ID of the book to delete
    :type book_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_all_books():  # noqa: E501
    """Get all books

     # noqa: E501


    :rtype: List[Book]
    """
    return 'do some magic!'


def get_book(book_id):  # noqa: E501
    """Get a book

     # noqa: E501

    :param book_id: ID of the book to retrieve
    :type book_id: int

    :rtype: Book
    """
    return 'do some magic!'


def update_book(body, book_id):  # noqa: E501
    """Update a book

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param book_id: ID of the book to update
    :type book_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = Book.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

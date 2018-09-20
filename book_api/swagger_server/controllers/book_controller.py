import connexion
import six

from swagger_server.models.book import Book  # noqa: E501
from swagger_server import util


def add_book(body):  # noqa: E501
    """Adds a new book to the store

     # noqa: E501

    :param body: Book object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Book.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_book_by_id(bookId):  # noqa: E501
    """Deletes a Book

     # noqa: E501

    :param bookId: Book id to delete
    :type bookId: int

    :rtype: None
    """
    return 'do some magic!'


def get_book_by_id(bookId):  # noqa: E501
    """Finds book by ID

    Returns a single book # noqa: E501

    :param bookId: ID of Book to return
    :type bookId: int

    :rtype: Book
    """
    return 'do some magic!'


def update_book_by_id(bookId):  # noqa: E501
    """Updates a Book given an id 

     # noqa: E501

    :param bookId: ID of Book that needs to be updated
    :type bookId: int

    :rtype: None
    """
    return 'do some magic!'

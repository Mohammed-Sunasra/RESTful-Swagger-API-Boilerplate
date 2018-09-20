# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.book import Book  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBookController(BaseTestCase):
    """BookController integration test stubs"""

    def test_add_book(self):
        """Test case for add_book

        Adds a new book to the store
        """
        body = Book()
        response = self.client.open(
            '/v2/book',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_book_by_id(self):
        """Test case for delete_book_by_id

        Deletes a Book
        """
        response = self.client.open(
            '/v2/book/{bookId}'.format(bookId=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_book_by_id(self):
        """Test case for get_book_by_id

        Finds book by ID
        """
        response = self.client.open(
            '/v2/book/{bookId}'.format(bookId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_book_by_id(self):
        """Test case for update_book_by_id

        Updates a Book given an id 
        """
        response = self.client.open(
            '/v2/book/{bookId}'.format(bookId=789),
            method='PUT',
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

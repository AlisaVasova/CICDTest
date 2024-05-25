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

        Add a new book
        """
        body = Book()
        response = self.client.open(
            '//books',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_book(self):
        """Test case for delete_book

        Delete a book
        """
        response = self.client.open(
            '//books/{bookId}'.format(book_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_books(self):
        """Test case for get_all_books

        Get all books
        """
        response = self.client.open(
            '//books',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_book(self):
        """Test case for get_book

        Get a book
        """
        response = self.client.open(
            '//books/{bookId}'.format(book_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_book(self):
        """Test case for update_book

        Update a book
        """
        body = Book()
        response = self.client.open(
            '//books/{bookId}'.format(book_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

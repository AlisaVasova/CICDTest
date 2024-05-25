from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.host = 'http://192.168.0.29:8080/'
api_client = swagger_client.ApiClient(configuration=configuration)
api_instance = swagger_client.BookApi(api_client=api_client)
body = swagger_client.Book() # Book |

try:
    # Add a new book
    api_instance.add_book(body)
except ApiException as e:
    print("Exception when calling BookApi->add_book: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.BookApi(swagger_client.ApiClient(configuration))
book_id = 56 # int | ID of the book to delete

try:
    # Delete a book
    api_instance.delete_book(book_id)
except ApiException as e:
    print("Exception when calling BookApi->delete_book: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.BookApi(swagger_client.ApiClient(configuration))

try:
    # Get all books
    api_response = api_instance.get_all_books()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookApi->get_all_books: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.BookApi(swagger_client.ApiClient(configuration))
book_id = 56 # int | ID of the book to retrieve

try:
    # Get a book
    api_response = api_instance.get_book(book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookApi->get_book: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.BookApi(swagger_client.ApiClient(configuration))
body = swagger_client.Book() # Book |
book_id = 56 # int | ID of the book to update

try:
    # Update a book
    api_instance.update_book(body, book_id)
except ApiException as e:
    print("Exception when calling BookApi->update_book: %s\n" % e)
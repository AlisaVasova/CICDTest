# swagger_client.BookApi

All URIs are relative to *https://api.bookreader.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_book**](BookApi.md#add_book) | **POST** /books | Add a new book
[**delete_book**](BookApi.md#delete_book) | **DELETE** /books/{bookId} | Delete a book
[**get_all_books**](BookApi.md#get_all_books) | **GET** /books | Get all books
[**get_book**](BookApi.md#get_book) | **GET** /books/{bookId} | Get a book
[**update_book**](BookApi.md#update_book) | **PUT** /books/{bookId} | Update a book

# **add_book**
> add_book(body)

Add a new book

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BookApi()
body = swagger_client.Book() # Book | 

try:
    # Add a new book
    api_instance.add_book(body)
except ApiException as e:
    print("Exception when calling BookApi->add_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Book**](Book.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_book**
> delete_book(book_id)

Delete a book

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BookApi()
book_id = 56 # int | ID of the book to delete

try:
    # Delete a book
    api_instance.delete_book(book_id)
except ApiException as e:
    print("Exception when calling BookApi->delete_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**| ID of the book to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_books**
> list[Book] get_all_books()

Get all books

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BookApi()

try:
    # Get all books
    api_response = api_instance.get_all_books()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookApi->get_all_books: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Book]**](Book.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_book**
> Book get_book(book_id)

Get a book

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BookApi()
book_id = 56 # int | ID of the book to retrieve

try:
    # Get a book
    api_response = api_instance.get_book(book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookApi->get_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**| ID of the book to retrieve | 

### Return type

[**Book**](Book.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_book**
> update_book(body, book_id)

Update a book

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BookApi()
body = swagger_client.Book() # Book | 
book_id = 56 # int | ID of the book to update

try:
    # Update a book
    api_instance.update_book(body, book_id)
except ApiException as e:
    print("Exception when calling BookApi->update_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Book**](Book.md)|  | 
 **book_id** | **int**| ID of the book to update | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


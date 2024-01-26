# Bookstore API
This API provides CRUD (Create, Read, Update, Delete) operations for managing books in a bookstore. Users must authenticate using JWT (JSON Web Token) to access certain endpoints.

**Full Documentation** - https://documenter.getpostman.com/view/32317791/2s9YypFit8

## API Guide
- Auth
  - /auth
    - This endpoint is used to authenticate users via HTTP POST request to localhost:8000/auth. The request should include a payload in raw JSON format with "username" and "password" fields. Upon successful execution, the endpoint returns a status code of 201 and a JSON response with a "message" field indicating the outcome of the authentication process.
  - /auth/token
    - This endpoint is used to authenticate and obtain a token for accessing protected resources.
- CRUD
  - GET: /books
    - This endpoint retrieves a list of books.
  - GET: /book/{isbn}
    - This endpoint makes an HTTP GET request to localhost:8000/book/5678 to retrieve information about a specific book with the given ISBN. The response will be in JSON format and will include the title, ISBN, author, quantity, and price of the book.
  - POST: /books
    - This endpoint allows you to add a new book to the collection.
  - PUT: /book/{isbn}
    - This endpoint allows you to update a book with the specified ID.
  - DELETE: /book/{isbn}
    - This endpoint sends an HTTP DELETE request to localhost:8000/book/1234567901 to delete a specific book. Upon successful deletion, it returns a JSON response with a status code of 200 and a message indicating the success of the operation.
     
## Features
- Uses python & FastAPI
- JWT Authentication
- Unit Tests for each endpoint
- MySQL Database

# SignEasy_API
SignEasy Assignment

Read documentation.txt for 
* pre-requirements
* Assumptions made
* Database setup
* Schema

REST Endpoints:
Pre Requisite: use postman to view pretty json

GET http://localhost:8000/api/v1/books							---------------> Retrieve all books
POST http://localhost:8000/api/v1/books							---------------> Create the books
DELETE http://localhost:8000/api/book/<book_id>/				---------------> DELETE the books

GET http://localhost:8000/api/v1/members						---------------> Retrieve all users
POST http://localhost:8000/api/v1/members						---------------> Add the user
DELETE http://localhost:8000/api/member/<book_id>/				---------------> DELETE the books

GET http://localhost:8000/api/borrow/<book_id>/					---------------> Borrow the books
GET http://localhost:8000/api/return/<book_id>/					---------------> Return the books


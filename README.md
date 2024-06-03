# Book Reading Library API (Backend Only)
This is my Web stack Specialization portfolio project for my ALX Software Engineering program. Having specialized on Back End I opted to develop the backend of the app.

## Introduction
In this project, which aims to enhance the book reading experience, I will tackle the challenges I face during the reading process and how I intend to address them through the development of an interactive app. The app will provide features such as scheduling, goal-setting, progress tracking, and book recommendations.

In this project I have developed a RESTful API built for the Book reading (BookApi) application. Its code is built with Python and the Flask Web Framework. It responds to authenticated front-end requests and connects to a NoSQL database (MongoDB). Some of its files contain configurations for deployment through Nginx


# A Simple Book Reading Library API

Simple HTTP API for playing with `Book` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `book.py`: book model
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/books.py`: all books endpoints
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /get_users`: returns the list of users
- `GET /get_books`: returns the list of books
- `GET /get_user/:id`: returns a user based on the ID
- `GET /get_book/:id`: returns a book based on the ID
- `DELETE /delete_user/:id`: deletes an user based on the ID
- `DELETE /delete_book/:id`: deletes a book based on the ID
- `POST /add_book`: creates a new book (JSON parameters: `title`, `author`, `isbn` (optional) and `publisher` (optional))
- `POST /add_user`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /update_user/:id`: updates a user based on the ID (JSON parameters: `first_name` and `last_name`)
- `PUT /update_book/:id`: updates a book based on the ID (JSON parameters: `title` and `author`)

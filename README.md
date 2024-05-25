# Book Reading Library API (Backend Only)
This is my Web stack Specialization portfolio project for my ALX Software Engineering program. Having specialized on Back End I opted to develop the backend of the app.

## Introduction
In this project, which aims to enhance the book reading experience, I will tackle the challenges I face during the reading process and how I intend to address them through the development of an interactive app. The app will provide features such as scheduling, goal-setting, progress tracking, and book recommendations. Current focus is on it's backend development first with UI designs to follow.

This project seeks to bridge the gap between traditional reading practices and modern technological conveniences. The app will offer a user-friendly interface, making it accessible for users of all ages and technical proficiencies. Whether it’s tracking personal progress, discovering new books, or synchronizing reading schedules with fellow book club members, the app aims to become an essential companion for every reader’s journey.

# Simple API

Simple HTTP API for playing with `Book` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
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
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/books`: returns the list of books
- `GET /api/v1/users/:id`: returns a user based on the ID
- `GET /api/v1/books/:id`: returns a book based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `DELETE /api/v1/books/:id`: deletes a book based on the ID
- `POST /api/v1/users`: creates a new book (JSON parameters: `title`, `author`, `isbn` (optional) and `publisher` (optional))
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates a user based on the ID (JSON parameters: `first_name` and `last_name`)
- `PUT /api/v1/book/:id`: updates a book based on the ID (JSON parameters: `title` and `author`)
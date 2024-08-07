# Book Management Application

## Description

The Book Management Application is a web application that allows users to manage a collection of books. Users can view,
add, and delete books. The application is built using Flask and SQLAlchemy, with SQLite as the database.

## Installation

To get started with the Book Management Application, follow these steps:

Clone the repository:

```bash
git clone https://github.com/Leonardoloda/PythonPlayground.git
cd projects/LibraryLogger
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

The application will be accessible at http://127.0.0.1:8080.

## Usage

### Viewing Books

1. Navigate to the homepage (/books) to see a list of all books in the collection.

### Adding a Book

1. Navigate to the /add page.
2. Fill out the form with the book's name, author, and rating.
3. Submit the form to add the book to the collection.

### Deleting a Book

1. Navigate to the /books/<book_id> page, where <book_id> is the ID of the book you want to delete.
   The book will be removed from the collection, and you will be redirected to the homepage.

## Features

- **View Books:** Displays a list of all books in the collection.
- **Add Book:** Allows users to add a new book to the collection.
- **Delete Book:** Allows users to delete a book from the collection.

## Technologies

- **ORM:** Utilizes SQLAlchemy as an ORM to map tables and handle database operations.
- **Templates:** Uses Jinja2 templates to render HTML pages.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request.
Acknowledgments
Flask: https://flask.palletsprojects.com/
SQLAlchemy: https://www.sqlalchemy.org/
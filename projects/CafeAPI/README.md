# Cafe Management Application

## Table of Content

- [Table of Content](#table-of-content)
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
  - [Viewing All Cafes](#viewing-all-cafes)
  - [Fetching a Random Cafe](#fetching-a-random-cafe)
  - [Searching for Cafes by Location](#searching-for-cafes-by-location)
  - [Adding a New Cafe](#adding-a-new-cafe)
  - [Updating Cafe Coffee Price](#updating-cafe-coffee-price)
  - [Deleting a Cafe](#deleting-a-cafe)
- [Features](#features)
- [Contributing](#contributing)

## Description

The Cafe Management Application is a Flask-based web application that allows users to manage a collection of cafes. Users can view, add, update, search, and delete cafes. The application uses SQLAlchemy for database interactions and SQLite as the database backend.

## Installation

To get started with the Book Management Application, follow these steps:

Clone the repository:

```bash
git clone https://github.com/Leonardoloda/PythonPlayground.git
cd projects/CafeAPI
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

### Viewing All Cafes

Make a GET request to /cafes to view a list of all cafes in the collection.

### Fetching a Random Cafe

Make a GET request to /random to get a random cafe from the database.

### Searching for Cafes by Location

Make a GET request to /search?location=LocationName to search for cafes by their location.

### Adding a New Cafe

Send a POST request to /cafe with the following form data to add a new cafe:

- `name`: The name of the cafe.
- `map_url`: The Google Maps URL of the cafe.
- `img_url`: The image URL of the cafe.
- `location`: The location of the cafe.
- `has_sockets`: 1 if the cafe has power sockets, otherwise 0.
- `has_toilet`: 1 if the cafe has a toilet, otherwise 0.
- `has_wifi`: 1 if the cafe has Wi-Fi, otherwise 0.
- `can_take_calls`: 1 if the cafe allows taking calls, otherwise 0.
- `seats`: The seating capacity of the cafe.
- `coffee_price`: The price of coffee at the cafe.

### Updating Cafe Coffee Price

Send a PATCH request to /price/<int:cafe_id> with the following form data to update the coffee price for a specific cafe:

- `price`: The new coffee price.

### Deleting a Cafe

Send a DELETE request to /cafe/<int:cafe_id> to delete a specific cafe by its ID.

## Features

- **View Cafes:** Displays a list of all cafes in the collection.
- **Add Cafe:** Allows users to add a new cafe to the collection.
- **Update Cafe:** Updates the price of coffee for a specific cafe.
- **Delete Cafe:** Deletes a cafe from the collection.
- **Search Cafes:** Search for cafes by location.
- **Fetch Random Cafe:** Retrieves a random cafe from the collection.
- **ORM:** Utilizes SQLAlchemy as an ORM to map tables and handle database operations.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request.

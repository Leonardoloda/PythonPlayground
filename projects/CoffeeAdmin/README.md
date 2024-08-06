# Cafe Franchises Inventory App

## Description

The Cafe Franchises Inventory App is a web application designed to manage and view all existing cafes in a franchise.
This application is built using Flask, Flask-WTF for form handling, and Bootstrap-Flask for rendering forms. The cafe
data is stored and managed using pandas in a CSV file.

## Installation

To get started with the Cafe Franchises Inventory App, follow these steps:

Clone the repository:

```bash
git clone https://github.com/yourusername/cafe-inventory-app.git
cd projects/CoffeeAdmin
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
flask run
```

The application will be accessible at http://127.0.0.1:8080.

## Usage

### Adding a New Cafe

1. Navigate to `/add`.
2. Fill out the form to add a new cafe.
3. Submit the form to save the new cafe details.

### Viewing Existing Cafes

1. Navigate to the "Show Cafes" page.
2. Browse the list of all existing cafes in the franchise.

## Features

- **Add Cafe:** Allows users to add new cafes to the inventory.
- **View Cafes:** Displays a list of all existing cafes in the franchise.
- **CSV Storage:** Uses pandas to manage cafe data stored in a CSV file.
- **Form Handling:** Utilizes Flask-WTF for secure and easy form handling.
- **Bootstrap Integration:** Leverages Bootstrap-Flask for responsive and aesthetically pleasing forms.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request.
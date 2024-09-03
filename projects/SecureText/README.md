# Secure Note Sharing Application

## Description

The Secure Note Sharing Application is a Flask-based web app that allows users to create and share notes securely. Once
a note is read, it is automatically deleted from the database, ensuring that the content can only be viewed once.

## Running the application

To run this application, run the next script in your console

```bash
    python main.py
```

The application will be accessible at `http://127.0.0.1:8080`.

## Usage

### Home Page

The home page will redirect you to the `/create` page where you can create a new note.

### Creating a Note

- Navigate to `/create` to create a new note.
- Enter the content of the note in the provided form and submit it.
- After submission, you will receive a unique link that you can share with others.

### Viewing a Note

- When the recipient visits the link, the note's content will be displayed, and the note will be automatically deleted
  from the database.

### One-Time View

- **Important:** Once a note is viewed, it is permanently deleted from the database and cannot be accessed again.

## Key Features

- **Secure Sharing:** Once a note is viewed, it is permanently deleted, ensuring the content remains private.
- **Unique Links:** Each note is assigned a unique link that can be shared with others.
- **Database Integration:** Uses SQLAlchemy to manage notes in a database.
- **Bootstrap Integration:** Leverages Flask-Bootstrap for responsive and clean front-end design.

## Contributing

We welcome contributions to the Secure Note Sharing Application! To contribute, follow these steps:

1. **Fork and clone the repository:**

    ```bash
    git clone https://github.com/yourusername/secure-note-sharing.git
    ```

2. **Create a new branch for your changes:**

    ```bash
    git checkout -b my-feature
    ```

3. **Make your changes and commit them:**

    ```bash
    git commit -am 'Add new feature'
    ```

4. **Push to your branch:**

    ```bash
    git push origin my-feature
    ```

5. **Open a pull request:**

   Go to the original repository on GitHub and click "New Pull Request."

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

For any issues or questions, please open an issue on the repository or contact the maintainer.

Enjoy sharing your notes securely with the Secure Note Sharing Application!
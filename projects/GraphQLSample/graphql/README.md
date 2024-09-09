# GraphQL Posts

## Description

This project is a GraphQL API built using Apollo Server, integrating Flask and PostgreSQL. It follows a schema-first
approach to define the API schema and write resolvers for querying and mutating data. It includes basic functionality
such as creating, updating, retrieving, and deleting records from a PostgreSQL database using GraphQL queries and
mutations.

## Requirements

Make sure to install the necessary dependencies before running the project.

### Install dependencies:

```bash
pip install -r requirements.txt
```

Add the following libraries to `requirements.txt` if needed:

- **Flask** – Web framework
- **Flask-SQLAlchemy** – ORM for managing the database
- **Ariadne** – GraphQL library for schema and resolvers
- **Flask-CORS** – Cross-Origin Resource Sharing for handling client-server communication

## Usage

1. **Set Up Environment Variables**:

   Make sure to create a `.env` file with your PostgreSQL database URL:

   ```
   DATABASE_URL=your_database_url
   ```

2. **Run the Application**:

   Start the server with the following command:

   ```bash
   flask run
   ```

   The GraphQL playground will be available at `http://localhost:5000/graphql`.

3. **Sample GraphQL Query**:

    - To fetch all posts:

      ```graphql
      query AllPosts {
        listPosts {
          success
          errors
          posts {
            id
            title
            description
            created_at
          }
        }
      }
      ```

4. **Sample GraphQL Mutation**:

    - To create a new post:

      ```graphql
      mutation CreateNewPost {
        createPost(title: "Sample Title", description: "Sample Description") {
          post {
            id
            title
            description
            created_at
          }
          success
          errors
        }
      }
      ```

## Contributing

Feel free to create a PR if you'd like to contribute!

## License

Free to use.

---

Enjoy building your GraphQL API with Apollo Server!
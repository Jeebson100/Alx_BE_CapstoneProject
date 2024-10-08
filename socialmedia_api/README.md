Social Media API

This is a simple Social Media API built with Django and Django REST Framework. It provides functionalities for user registration, login, posting content, following/unfollowing users, and more. The project also includes API documentation using Swagger and ReDoc.

Features
User registration, login, and logout
Create, view, update, and delete posts
Follow and unfollow other users
Token-based authentication
Pagination and filtering for posts
API documentation with Swagger and ReDoc

Requirements
Python 3.6+
Django 3.2+
Django REST Framework
SQLite (default database, but you can use others like PostgreSQL)

Setup Instructions
Step 1: Clone the repository
bash
Copy code
git clone <repository_url>
cd <project_directory>

Step 2: Create a virtual environment and activate it
It's best to run the project in a virtual environment to manage dependencies.
bash
Copy code
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On MacOS/Linux
source venv/bin/activate

Step 3: Install dependencies
Install the required Python packages from the requirements.txt file.

bash
Copy code
pip install -r requirements.txt
If you don't have a requirements.txt file yet, you can create one using:

bash
Copy code
pip freeze > requirements.txt

Step 4: Set up environment variables (optional but recommended)
Create a .env file in the project root directory and set environment variables like SECRET_KEY and database credentials (if you're not using SQLite).

bash
Copy code
# Example .env file
SECRET_KEY=your_secret_key_here
DEBUG=True

Step 5: Run migrations
Make sure the database is set up correctly by running migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate

Step 6: Create a superuser
If you want to access the Django admin interface, create a superuser by running:

bash
Copy code
python manage.py createsuperuser
Follow the instructions to create a superuser account.

Step 7: Start the server
Start the Django development server:

bash
Copy code
python manage.py runserver
By default, the server will be accessible at http://127.0.0.1:8000/.

Accessing the API
API Endpoints
Here are some example API endpoints:

Register a new user: POST /register/
Login: POST /api-token-auth/
Create a new post: POST /posts/
View all posts: GET /posts/
Follow a user: POST /follow/{username}/
Unfollow a user: POST /unfollow/{username}/
Authentication
Use token-based authentication. After logging in, you will receive an authentication token. Use this token in the header of requests:

bash
Copy code
Authorization: Token your_token_here
API Documentation
API documentation is available using Swagger and ReDoc.

Swagger
Access the Swagger UI documentation at:

arduino
Copy code
http://127.0.0.1:8000/swagger/
ReDoc
Access the ReDoc documentation at:

arduino
Copy code
http://127.0.0.1:8000/redoc/
Testing
To ensure that all the features are working correctly, you can test the API endpoints using a tool like Postman or curl.

Example: Register a user
bash
Copy code
curl -X POST http://127.0.0.1:8000/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "email": "test@example.com", "password": "password123"}'

Example: Create a post
bash
Copy code
curl -X POST http://127.0.0.1:8000/posts/ \
  -H "Authorization: Token your_token_here" \
  -H "Content-Type: application/json" \
  -d '{"content": "This is my first post!"}'

Deployment (Optional)
If you plan to deploy the API to production, make sure to:

Set DEBUG = False in settings.py or .env.
Use a production-ready database like PostgreSQL.
Configure the server to serve static files (e.g., using nginx).
Ensure that your secret key and other sensitive configurations are stored in environment variables.
License
This project is licensed under the BSD License. See the LICENSE file for more details.

Contact
For any inquiries or issues, contact the developer:

Email: jeebson100@gmail.com

Final Notes:
Update <repository_url> and <project_directory> with the actual values.
Ensure your .env file is set up if you use it for production settings (e.g., SECRET_KEY, database credentials).
Make sure requirements.txt includes all necessary dependencies (e.g., Django, DRF, Swagger libraries).
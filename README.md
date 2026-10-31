# Secure Notes API

A RESTful backend application built with Python and FastAPI to manage personal notes through secure user authentication and access control.

## About the Project

Secure Notes API provides authenticated users with a way to create, retrieve, update and delete their personal notes.

The application uses JWT-based authentication to protect private endpoints and associates each note with its respective user.

## Key Features

- User registration and login
- Secure password hashing
- JWT-based authentication
- Create, read, update and delete notes (CRUD)
- User-specific note access
- Request validation using Pydantic
- SQLite database integration
- Interactive API documentation

## Technology Stack

| Technology | Usage |
|---|---|
| Python | Programming language |
| FastAPI | Backend framework |
| SQLAlchemy | Database ORM |
| SQLite | Database |
| Pydantic | Data validation |
| JWT | User authentication |
| Passlib / bcrypt | Password hashing |
| Uvicorn | Application server |

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Log in and receive an access token |

### Notes

| Method | Endpoint | Description |
|---|---|---|
| POST | `/notes/` | Create a new note |
| GET | `/notes/` | Retrieve all personal notes |
| GET | `/notes/{note_id}` | Retrieve a specific note |
| PUT | `/notes/{note_id}` | Update an existing note |
| DELETE | `/notes/{note_id}` | Delete a note |

All note endpoints require valid authentication.

## Project Structure

```text
Secure_notes_api/
│
├── app/
│   ├── routers/
│   │   ├── auth.py
│   │   └── notes.py
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── security.py
│   ├── deps.py
│   └── config.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python installed
- Git installed

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd Secure_notes_api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root and configure the variables required by the application, including a newly generated secret key.

Never commit your `.env` file to GitHub.

### 6. Start the server

```bash
uvicorn app.main:app --reload
```

## API Documentation

After starting the server, access:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Security

- Passwords are stored as hashes.
- Protected routes require JWT authentication.
- Each note is associated with its owner's user ID.
- Users cannot access or modify notes belonging to other users.

## Future Enhancements

- Automated testing with Pytest
- Pagination and note search
- Refresh-token implementation
- Rate limiting
- Cloud deployment

## Author

Developed as a backend development project to practise REST API development, authentication, database operations and application security.
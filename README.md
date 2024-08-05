# DRF Starter Kit

Welcome to the DRF Starter Kit! This repository provides a boilerplate for quickly starting a Django project with Django REST Framework (DRF). It includes essential features such as API authentication with access and refresh tokens, role-based access control (RBAC), Swagger documentation, API versioning, pagination, custom response formats, and a custom exception handler. Additionally, it includes the Django built-in admin panel for managing your application.

## Features

- **Django REST Framework (DRF)**: A powerful and flexible toolkit for building Web APIs.
- **API Authentication**: Access and refresh tokens for secure authentication.
- **RBAC (Role-Based Access Control)**: Fine-grained control over user permissions.
- **Swagger**: Interactive API documentation.
- **API Versioning**: Support for versioned APIs.
- **Pagination**: Efficient handling of large datasets.
- **Custom Response**: Standardized response format.
- **Custom Exception Handler**: Centralized error handling.
- **Django Admin Panel**: Built-in admin interface for managing the application.


## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/hashirventhodi/drf-starter-kit.git
    cd drf-starter-kit
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements/development.txt
    ```

4. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

## Configuration

- **Environment Variables**: Configure your environment variables in a `.env` file.
    ```
    DEBUG=True
    SECRET_KEY=your_secret_key
    DATABASE_URL=postgres://user:password@localhost:5432/yourdb
    ```

- **Database**: By default, this project is configured to use PostgreSQL. Update `DATABASES` in `settings.py` if needed.

## Usage
- Access the admin interface at `http://localhost:8000/admin/` to manage data.
- Use the API endpoints for programmatic access.

### API Documentation

- **Swagger**: Access the interactive API documentation at `/swagger/`.

### API Versioning

- This starter kit uses URL path versioning. Example: `/api/v1/`.

### Pagination

- Pagination is enabled globally. Configure `PAGE_SIZE` in `settings.py`.

### Custom Response Format

- All responses follow a standardized format:
    ```json
    {
        "status": "success",
        "data": {...}
    }
    ```

### Custom Exception Handler

- Centralized error handling with a consistent response format:
    ```json
    {
        "status": "error",
        "message": "An error occurred"
    }
    ```

## Project Structure
```
project_name/
│
├── apps/
│   ├── app1/
│   │   ├── v1/
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   └── urls.py
│   │   ├── models.py
│   │   └── tests.py
│   ├── app2/
│   │   └── ...
│   └── ...
│
├── core/
│   ├── settings/
│   │   ├── base.py           # Base settings
│   │   ├── development.py    # Development settings
│   │   └── production.py     # Production settings
│   ├── urls.py               # Root URL configuration
│   └── wsgi.py               # WSGI config for deployment
│
├── utils/
│   ├── mixins.py             # Utility mixins
│   ├── permissions.py        # Custom permissions
│   └── ...                   # Other utility files
│
├── manage.py                  # Django's command-line utility
├── requirements/              # Directory for requirements files
│   ├── base.txt              # Base dependencies
│   ├── development.txt       # Development environment dependencies
│   └── production.txt        # Production environment dependencies
│
├── README.md                  # Project documentation
├── LICENSE                    # License information
└── .gitignore                 # Git ignore file

```


## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact [Hashir V](mailto:hashirventhodi@example.com).


# Django Base with Custom User and JWT Authentication

This repository provides a Django project base with a custom user model and an authentication system implemented using Djoser and JWT.

## Features

- **Custom User:** A custom user model has been implemented, extending Django's default user model.

- **JWT Authentication with Djoser:** The authentication system uses Djoser to provide registration, login, password recovery, etc. endpoints and utilizes JSON Web Tokens (JWT) to authenticate requests.

## Requirements

- Python
- Django
- Djoser
- Rest framework
- Other requirements as specified in `requirements.txt`

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/yourrepo.git
    cd yourrepo
    ```

2. Create a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Unix-like systems
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

5. Visit `http://localhost:8000` in your browser.

## Usage

You can start building your application on this base. Check [Djoser's documentation](https://djoser.readthedocs.io/en/latest/) to understand how to use the provided endpoints for authentication.


## Contribute

Contributions are welcome! If you find bugs or potential improvements, open an issue or send a pull request.

## License

This project is under the MIT License - see the [LICENSE](LICENSE) file for more details.

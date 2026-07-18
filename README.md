# Django Mini Shop with Tastypie API 🎓

A simple course shop built with **Django** and **Django Tastypie**.

The project demonstrates how to create and manage an API using Tastypie. Courses can be managed through the Django Admin Panel or via API requests using tools like Postman.

## Features

- 📚 Display all courses
- 📄 Course details
- 🏷 Categories
- ➕ Create courses via API
- ❌ Delete courses via API
- 🔐 Authentication for API requests
- ⚙ Django Admin Panel
- 🧪 Postman support

## Technologies

- Python
- Django
- Django Tastypie
- SQLite3
- HTML
- CSS
- Bootstrap
- Postman

## Project Structure

```text
django-api/
│
├── api/                # Tastypie resources
├── base/               # Django project
├── shop/               # Shop application
├── templates/
│   └── shop/
├── manage.py
└── requirements.txt
```

## Installation

```bash
git clone https://github.com/Anvarjon0038/django-api.git

cd django-api

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```

## Admin Panel

```
http://127.0.0.1:8000/admin/
```

Using the admin panel you can:

- Add categories
- Add courses
- Edit courses
- Delete courses

---

# Tastypie API

Base URL

```
http://127.0.0.1:8000/api/v1/
```

## Categories

| Method | Endpoint |
|--------|----------|
| GET | `/api/v1/categories/` |
| GET | `/api/v1/categories/<id>/` |

## Courses

| Method | Endpoint |
|--------|----------|
| GET | `/api/v1/courses/` |
| GET | `/api/v1/courses/<id>/` |
| POST | `/api/v1/courses/` |
| DELETE | `/api/v1/courses/<id>/` |

## Example JSON

```json
{
    "title": "Cpp Guide",
    "price": 120,
    "description": "Learn Cpp from scratch",
    "category_id": 1
}
```

## Authentication

Creating and deleting courses requires authentication using the custom Tastypie authentication class

## Testing

The API can be tested with:

- Postman
- Insomnia
- cURL

> **Note**
>
> Browsers can only be used to test **GET** endpoints.
> To create or delete courses, use an API client such as **Postman**, **Insomnia**, or **cURL**, because these operations require authenticated **POST** and **DELETE** request

## Author

**Anvarjon Toshmatov**

GitHub: https://github.com/Anvarjon0038

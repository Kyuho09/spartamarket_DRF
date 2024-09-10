## Project name
Sparta Market Implemented by Django REST Framework

## Introduction
Spartamarket_DRF is a simple used market service implemented using Django and Django REST Framework. It provides user registration, login, profile, product posting, inquiry, modification, and deletion.

## Development Period
- Start Date: 2024.09.05
- End Date: 2024.09.10

## Full Technology Stack Overview
- Programming Language: python 3.10
- Web Framework: Django 4.2
- Database: SQLite
- IDE: PyCharm, Vs code
- Version Control: Git, Github
- Technical stack
  - Backend: Python, Django
  - Database: Django ORM, SQLite

<br>

## Key Features

- **Sign Up**:
  - Users can sign up by providing a username, password, nickname, birthdate, and gender.
  ![Sign Up](https://github.com/Kyuho09/spartamarket_DRF/blob/main/images/signup.png?raw=true)

- **Log In**:
  - Users can log in using their username and password with JWT-based authentication.
  - After logging in, users gain access to additional features that require authentication.
  ![Log In](https://github.com/Kyuho09/spartamarket_DRF/blob/main/images/login.png?raw=true)

- **Profile View**:
  - Users can view their own profile, including their registered posts.
  - Profile information includes nickname, birthdate, gender, and other personal details.
  ![Profile View](https://github.com/Kyuho09/spartamarket_DRF/blob/main/images/profile.png?raw=true)

- **Create Post**:
  - Users can create a new post by providing a product title, description, and images.
  - The created post is added to the product listing.
  ![Create Post](https://github.com/Kyuho09/spartamarket_DRF/blob/main/images/create.png?raw=true)

- **View Post List**:
  - All users can browse through the product listing, which displays posts in chronological order, with the most recent posts shown first.
  ![Post List](https://github.com/Kyuho09/spartamarket_DRF/blob/main/images/list.png?raw=true)

- **View Post Details**:
  - Users can view detailed information about individual posts.
  - Each post includes the title, description, images, and the date it was created.
  ![Post Details](https://github.com/Kyuho09/spartamarket_DRF/blob/main/images/detail.png?raw=true)

- **Edit Post**:
  - Post authors can edit their own posts, modifying the title, description, and images.
  - Only the author of the post is allowed to make edits, and unauthorized users cannot edit the post.
  ![Edit Post](https://github.com/Kyuho09/spartamarket_DRF/blob/main/images/update.png?raw=true)

- **Delete Post**:
  - Post authors can delete their own posts.
  - Once a post is deleted, it is removed from the product listing and can no longer be viewed.
  ![Delete Post](https://github.com/Kyuho09/spartamarket_DRF/blob/main/images/delete.png?raw=true)
  ![Delete Post Confirm](https://github.com/Kyuho09/spartamarket_DRF/blob/main/images/deleteadd.png?raw=true)

## Folder Structure
```bash
SPARTAMARKET_DRF
│
├── accounts/           # User authentication and management app
│   ├── migrations/     # Database migration files for accounts app
│   ├── __init__.py     
│   ├── models.py       # User model (customized)
│   ├── serializers.py  # User-related serializers
│   ├── urls.py         # URLs for user-related actions
│   ├── views.py        # Views for signup, signin, and profile
│   └── validators.py   # Validation logic for signup
│
├── products/           # App managing products CRUD operations
│   ├── migrations/     # Database migration files for products app
│   ├── __init__.py     
│   ├── models.py       # Product model definition
│   ├── serializers.py  # Product-related serializers
│   ├── urls.py         # URLs for product actions
│   └── views.py        # Views for product listing, detail, update, and delete
│
├── spartamarket/       # Project configuration files
│   ├── __init__.py     
│   ├── settings.py     # Project-wide settings
│   ├── urls.py         # Root URL configuration
│   └── wsgi.py         # WSGI configuration
│
├── db.sqlite3          # SQLite database file
├── manage.py           # Django management command file
├── .gitignore          # Files and directories to be ignored by Git
├── requirements.txt    # List of dependencies for the project

```
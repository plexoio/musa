## [HOME | RETURN](https://github.com/plexoio/musa/blob/main/documentation/readme/erd/erd.md)

## Project Setup Guide

### 1. Installation

### Install Django and Essential Libraries
```bash
pip3 install 'django<4' gunicorn psycopg2
```

**Key Components:**
- `Django_Project`
- `App` (Following the MVT pattern)
- `Requirements.txt`: Generate using `pip3 freeze --local > requirements.txt`
- `Env.py`

### 2. Initializing Django Project and App

1. Set up a new Django project and app:
```bash
django-admin startproject djangopost .
python3 manage.py startapp blog
```
**Note:** Remember to include the app in `INSTALLED_APPS` within `settings.py`.

2. Execute initial migrations:
```bash
python3 manage.py makemigrations --dry-run
python3 manage.py migrate
```

### 3. Configuration

#### 3.1 PostgreSQL and Cloudinary Libraries
```bash
pip3 install dj3-cloudinary-storage dj_database_url psycopg2
```

#### 3.2 Database Setup
- Create a new database on [ElephantSQL](https://customer.elephantsql.com/login).

#### 3.3 Adjust Allowed Hosts
To address the `DisallowedHost at /` error, update `ALLOWED_HOSTS` in `settings.py`.

#### 3.4 Cloudinary Configuration
For cloudinary integration, refer to Musa's or Djangopost's documentation.

#### 3.5 Environment Variables (Env.py)
```python
import os
import cloudinary

os.environ["DATABASE_URL"] = 'your_database_url_here'
os.environ['CLOUDINARY_URL'] = 'your_cloudinary_url_here'
```

#### 3.6 Directory Structure
Create the following directories at the top level:
- `media`
- `static`
- `templates`

### 4. Deployment to Heroku

1. Create a `Procfile` with the content: 
```
web: gunicorn django_musa.wsgi:application
```

2. Installation and Deployment Commands:
```bash
curl https://cli-assets.heroku.com/install.sh | sh
heroku login -i
heroku create musa-blogs
```

**Environment Variables for Deployment:**
- `DATABASE_URL`
- `SECRET_KEY`
- `PORT`
- `CLOUDINARY_URL`
- `DISABLE_COLLECTSTATIC`
- `DEVELOPMENT`
- `HEROKU_HOSTNAME`

**Additional Resources:** Check out the [Google Doc Guide](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit) for a detailed walkthrough.
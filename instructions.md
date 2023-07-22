```markdown
## For All Projects

### 1. Install Django and Supporting Libraries
```bash
pip3 install 'django<4' gunicorn psycopg2
```

**Key Components:**
- `Django_Project`
- `App` (MVT)
- `Requirements.txt`: Use `pip3 freeze --local > requirements.txt`
- `Env.py`

### 2. Set Up an Empty Django Project and App
```bash
django-admin startproject djangopost .
python3 manage.py startapp blog
```
**Note:** After creating the app, add it to the `INSTALLED_APPS` in `settings.py`.

```bash
python3 manage.py migrate
```

### 3. Configuration for PostgreSQL and Cloudinary
```bash
pip3 install dj3-cloudinary-storage
pip3 install dj_database_url pyscopg2
```

#### 3.1 Create Database:
- Visit [ElephantSQL](https://customer.elephantsql.com/login)

### 3.2 Allow App

`ALLOWED_HOSTS = []` at settings.py, to tackle `DisallowedHost at /` error.
### 3.3 Templates & Cloudinary

See other examples a Musa's or Djangopost's documentation.

### 3.4 Env.py

    import os
    import cloudinary

    os.environ["DATABASE_URL"] = 'url'
    os.environ['CLOUDINARY_URL'] = 'url'
### 3.5 Create folder
Create 3 new folders on top level directory: media, static, templates
### 4. Deploy to Heroku
- Create a `Procfile`: web: gunicorn django_musa.wsgi:application

**Installation and Deployment:**
```bash
curl https://cli-assets.heroku.com/install.sh | sh
heroku login -i
heroku create musa-blogs
```

**Environment Variables:**
- `DATABASE_URL`
- `SECRET_KEY`
- `PORT`
- `CLOUDINARY_URL`
- `DISABLE_COLLECTSTATIC`
- `DEVELOPMENT`

**Additional Resources:** [Google Doc Guide](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit)
```

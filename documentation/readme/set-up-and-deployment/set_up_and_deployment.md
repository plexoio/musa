## [HOME | RETURN](https://github.com/plexoio/musa)

# Project Setup Guide & Deployment Process

## 1. Installation

### **Django and Essential Libraries**
Install Django (below version 4), along with necessary libraries.
```bash
pip3 install 'django<4' gunicorn psycopg2
```

#### **Key Components:** 
- **Project**: `Django_Project`
- **App**: `App` (Following the MVT pattern)
- **Dependencies**: Generate `Requirements.txt` with: 
```bash
pip3 freeze --local > requirements.txt
```
- **Environment Configuration**: `Env.py`

## 2. Initializing Django Project and App

### **Project and App Creation**
```bash
django-admin startproject djangopost .
python3 manage.py startapp blog
```
**Note:** Ensure to add the app in `INSTALLED_APPS` within `settings.py`.

### **Initial Migrations**
```bash
python3 manage.py makemigrations --dry-run
python3 manage.py migrate
```

## 3. Configuration

### **3.1 PostgreSQL and Cloudinary Libraries**
```bash
pip3 install dj3-cloudinary-storage dj_database_url psycopg2
```

### **3.2 Database Setup**
- Set up a new database on [ElephantSQL](https://customer.elephantsql.com/login).

### **3.3 Host Configuration**
To address the `DisallowedHost at /` error, modify `ALLOWED_HOSTS` in `settings.py`.

### **3.4 Cloudinary Integration**
Consult Musa's or Djangopost's documentation for comprehensive Cloudinary integration steps.

### **3.5 Environment Variables (`Env.py`)**
```python
import os
import cloudinary

os.environ["DATABASE_URL"] = 'your_database_url_here'
os.environ['CLOUDINARY_URL'] = 'your_cloudinary_url_here'
```

### **3.6 Directory Structure**
Ensure these top-level directories are in place:
- `media`
- `static`
- `templates`

## 4. Deployment to Heroku

### **Procfile Creation**
```bash
echo "web: gunicorn django_musa.wsgi:application" > Procfile
```

### **Heroku Installation and Deployment**
```bash
curl https://cli-assets.heroku.com/install.sh | sh
heroku login -i
heroku create musa-blogs
```

#### **Environment Variables for Deployment:** 
- `DATABASE_URL`
- `SECRET_KEY`
- `PORT`
- `CLOUDINARY_URL`
- `DISABLE_COLLECTSTATIC`
- `DEVELOPMENT`
- `HEROKU_HOSTNAME`

## Additional Resources
For a more comprehensive walkthrough, check out the [Google Doc Guide](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit).

## Commands used

- [Commands](https://github.com/plexoio/musa/blob/main/documentation/developer/commands.md): List of common commands used during development

# Deployment Process

To deploy our project, we'll utilize [Heroku](https://heroku.com/), an ideal platform for hosting and deploying web applications, as GitHub Pages doesn't support backend deployments.

## Pre-Deployment Preparation:

1. **Requirements File**: Ensure the `requirements.txt` file is in your project's root directory.
```bash
pip3 freeze > requirements.txt
```
2. If you haven’t already, sign up on [Heroku](https://heroku.com/).

## Setting Up on Heroku:

### Creating a New App:

1. Log in to the Heroku dashboard.
2. Click on `Create a new app`.
3. Name your app and select your region.
4. Press `Create App`.

### Configuring App Settings:

1. Navigate to the `Settings` section of your Heroku app.
2. Scroll to the `Config Vars` section.
    - Add Cloudinary environment variables: `CLOUDINARY_URL`, `CLOUDINARY_API_KEY`, and `CLOUDINARY_API_SECRET`.
    - Ensure your application is set to run on port 8000.

### Deploying to Heroku:

1. Go to the `Deploy` section.
2. Choose `GitHub` as the deployment method.
3. Connect Heroku to your GitHub and link your repository.
4. Under `Connect to GitHub`, find and select your repo. Click `Connect`.
5. You'll see both `Automatic Deploy` and `Manual Deploy` sections.
6. In `Manual Deploy`, make sure the main branch is selected and then click on `Deploy Branch`.
7. Once deployment is complete, you can click the `View` button to access your live application.

**Note**: Always ensure you've set the correct port for your application (port 8000) and have sufficient Heroku credits or an appropriate plan.
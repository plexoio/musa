## [HOME | RETURN](https://github.com/plexoio/musa/blob/main/documentation/readme/set-up-and-deployment/set_up_and_deployment.md)

# Essential Commands Guide

## **Django Management**

### **1. Creating a New App**
```bash
python manage.py startapp app_name
```

### **2. Interact with Django Shell**
```bash
python3 manage.py shell
```

### **3. Database Migrations**
- Generate migrations:
```bash
python3 manage.py makemigrations
```

- Preview migrations without making changes:
```bash
python3 manage.py makemigrations --dry-run
```

- Plan migrations:
```bash
python3 manage.py migrate --plan
```

- Apply migrations:
```bash
python3 manage.py migrate
```

## **Heroku Deployment**

### **1. Creating a Superuser on Heroku**
```bash
heroku run python manage.py createsuperuser
```

## **Package Management**

### **1. Generate Requirements File**
```bash
pip3 freeze --local > requirements.txt
```

### **2. Determine Python Version**
```bash
ls ../.pip-modules/lib
```

## **File Management**

### **1. Unzipping Files**
```bash
unzip static/font/roboto/roboto.zip
```

### **2. Copying Templates from Allauth**

- General copy:
```bash
cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/
```

- Copy to backend:
```bash
cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/backend
```
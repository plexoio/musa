heroku run python manage.py createsuperuser

pip3 freeze --local > requirements.txt

python3 manage.py makemigrations
python3 manage.py migrate --plan
python3 manage.py migrate
python3 manage.py makemigrations --dry-run


Know python version:
ls ../.pip-modules/lib


cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/

cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/backend
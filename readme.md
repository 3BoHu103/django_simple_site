# Django simple site streambook

## Steps:

- Clone this repository
```sh
git clone git@github.com:3BoHu103/django_simple_site.git
```
- Create .env file in settings folder and define environment variables.
```sh
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1 localhost [::1]
EMAIL_HOST_USER=your@gmail.com
EMAIL_HOST_PASSWORD=16charofpassword
EMAIL_FROM=your@gmail.com
DEFAULT_FROM_EMAIL=your@gmail.com
```
- Activate environ
```sh
source /env/bin/activate
```
- Install requirements
```sh
pip install -r requirements.txt
```
- Make migrations
```sh
python manage.py makemigrations
python manage.py migrate
```
- Create superuser
```sh
python manage.py createsuperuser
```

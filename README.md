EmenuRESTAPI 
===========

![alt text](https://github.com/marcin86junior/EmenuRESTAPI/blob/main/readme.PNG?raw=true)

Wymagania:

	Python 3.8.x
	Django 3.0.7

Instalacja:

	utwórz nowy katalog "PythonRestEmenu" i wejdz do niego
	git clone https://github.com/marcin86junior/EmenuRESTAPI .
	python -m venv myvenv
	.\myvenv\Scripts\activate
	pip install -r requirements.txt
	cd myproject\
	python manage.py migrate
	python manage.py createsuperuser
	python  manage.py loaddata eMenu\fixtures\data.json --app eMenu
	python manage.py runserver 

Testowanie:

	python manage.py test eMenu
	coverage run --source='.' --omit='*migrations*,*init*,*wsgi*,*asgi*,*urls*,*manage*,*admin*,*apps*,*settings*,*test*,*seriali*' manage.py test eMenu
	coverage html

Docker:

	utwórz nowy katalog "PythonRestEmenu" i wejdz do niego
	git clone https://github.com/marcin86junior/EmenuRESTAPI .
	cd myproject
	docker-compose up

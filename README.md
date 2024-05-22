Starting the Database
pg_ctl -D ./data/ -l logfile start

Stopping the database
pg_ctl -D ./data/ -l logfile stop


Running Django App
python manage.py runserver --nostatic

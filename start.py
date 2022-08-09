import os

os.system('docker-compose down')

if 'data' in os.listdir():
    os.system("sudo rm -r data")

os.system('docker-compose build')
os.system('docker-compose up -d')
os.system('docker-compose exec web python manage.py migrate')
os.system('docker-compose exec web python manage.py loaddata initial_data.json')
print('See => http://127.0.0.1:8000/')
print('To stop docker-compose => docker-compose down')

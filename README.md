
# Для запуска кейса, находясь в корне проекта прописать команду  

```
docker-compose up -d --build
```

# После запуска докера, находясь в корне проекта, прописать команды:

```
docker exec -it backend sh -c "python backend/manage.py makemigrations"
docker exec -it backend sh -c "python backend/manage.py migrate"
docker exec -it backend sh -c "python backend/manage.py createsuperuser" #создать пользователя для дальнейшей аутентификации
```


# Документация API по адресу http://127.0.0.1:8000/docs


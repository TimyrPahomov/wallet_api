# Wallet_API

Данный проект создан в качестве тестового задания в соответствии с техническим заданием.

Для **всех** пользователей реализованы следующие возможности:
- просмотр баланса кошелька;
- поплонение кошелька;
- вывод денежных средств с кошелька;

Добавлять и удалять кошельки могут только **администраторы**.

## Содержание
- [Технологии](https://github.com/TimyrPahomov/wallet_api#технологии)
- [Запуск с помощью Docker](https://github.com/TimyrPahomov/wallet_api#запуск-с-помощью-docker)
- [Создание суперпользователя](https://github.com/TimyrPahomov/wallet_api#создание-суперпользователя)
- [Доступ к проекту](https://github.com/TimyrPahomov/wallet_api#доступ-к-проекту)
- [Тестирование](https://github.com/TimyrPahomov/wallet_api#тестирование)
- [Автор](https://github.com/TimyrPahomov/wallet_api#автор)

## Технологии
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Docker](https://docs.docker.com/)

## Запуск с помощью Docker

1. Скачать Docker с [официального сайта](<https://www.docker.com/>), установить и запустить его.

2. Клонировать репозиторий и перейти в него:

```sh
git clone https://github.com/TimyrPahomov/wallet_api.git
cd test_task/
```

3. Далее нужно осуществить сборку контейнеров:

```sh
docker compose up
```

4. Затем следует открыть новый терминал, собрать статику приложения и выполнить миграции:

```sh
docker compose exec backend python manage.py collectstatic
docker compose exec backend python manage.py migrate
```

## Создание суперпользователя
Для создания суперпользователя нужно при запущенном в Docker приложении ввести в терминале команду:

```sh
docker compose exec backend python manage.py createsuperuser
``` 

## Доступ к проекту
У проекта реализованы следующие эндпоинты:

```sh
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/api/v1/wallets/<WALLET_UUID>/
http://127.0.0.1:8000/api/v1/wallets/<WALLET_UUID>/operation
```

## Тестирование
Проект покрыт тестами, для их запуска нужно при запущенном в Docker приложении ввести в терминале команду:

```sh
docker compose exec backend pytest
```

## Автор
[Пахомов Тимур](<https://github.com/TimyrPahomov/>)
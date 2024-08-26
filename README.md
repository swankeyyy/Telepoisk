<h2 align="center">KinoRandom</h2>
<br/>
[@mov_tele_bot](@mov_tele_bot)

KinoRandom - проект призванный помочь в одной из самых сложных задач сегодняшнего дня: выбору фильма на вечер.
Проект представляет собой несложный телеграм бот, который подбирает случайный фильм из коллекции автора, независимо от 
жанра и года производства. Автор обещает предлагать только интересные и рейтинговые фильмы.

Есть возможность добавлять фильм в список избранных, а так же возможность исключить фильм из предлагаемых.

Backend написан на DRF, новые фильмы добавляются автором.


![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python)
![Django](https://img.shields.io/badge/-Django-0aad48?style=flat-square&logo=Django)
![Django Rest Framework](https://img.shields.io/badge/DRF-red?style=flat-square&logo=Django)
![Postgresql](https://img.shields.io/badge/-Postgresql-%232c3e50?style=flat-square&logo=Postgresql)
![Docker](https://img.shields.io/badge/-Docker-46a2f1?style=flat-square&logo=docker&logoColor=white)
![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=flat-square&logo=telegram&logoColor=white)

## Старт

#### 1) Зарегестрировать бота в Телеграме(BotFather), получить токен

##### 2) В файле backend/telegram/.env.tg вставить полученный токен

#### 3) Создать образ
    cd backend
    docker-compose build

##### 4) Запустить контейнер

    docker-compose up

##### 5) Провести миграции

    docker-compose  exec web /bin/bash python manage.py migrate

##### 6) Создать администратора

    docker-compose  exec web /bin/bash python manage.py migrate

## Поддержка

По всем вопросам обращаться [swankyyy1@gmail.com](swankyyy1@gmail.com)
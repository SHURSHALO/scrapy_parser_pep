# Парсер PEP с использованием Scrapy

Данный проект предназначен для парсинга Python Enhancement Proposals (PEP) с использованием фреймворка Scrapy.

## Описание

Парсер PEP на основе Scrapy - это приложение на Python, разработанное для извлечения информации из PEP, размещенных на веб-сайте Python. Он использует фреймворк Scrapy для обхода индекса PEP и извлечения соответствующих деталей, таких как номер PEP, заголовок и статус.

## Установка

1. Клонировать репозиторий:

    git clone git@github.com:SHURSHALO/scrapy_parser_pep.git

2. Перейти в каталог проекта:

    cd scrapy_parser_pep


3. Установить необходимые зависимости с помощью pip:

    pip install -r requirements.txt


## Использование

Для запуска парсера PEP с помощью Scrapy выполните следующую команду:

scrapy crawl pep
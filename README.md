# bewiseQuiz - Сборка, настройка, запуск
## Зависимости

Для сборки Docker-образа вашего сервиса и его запуска, а также для отправки POST-запроса к API сервису, убедитесь что у вас есть все необходимые зависимости, такие как:

[Docker](https://docs.docker.com/get-docker/)
[Docker Compose](https://docs.docker.com/compose/install/)
[Poetry](https://python-poetry.org/docs/)
[Python](https://www.python.org/)

## Загрузка проекта

Клонируйте проект на свой компьютер (Используйте `dev` ветку для установки новой версии):

```bash
git clone https://github.com/lHACKERMANl/bewiseQuiz.git
cd bewiseQuiz/core
```

Весь основной код находится в папке `bewiseQuiz/core`. В нем будет происходить вся работа

## Сборка Docker-образа вручную

1. Выполните сборку Docker-образа приложения с помощью команды:

```bash
sudo docker compose --file docker_compose/app.yaml up --build
```

где `docker_compose/app.yaml` - это имя Docker-образа приложения. 

2. Выполните сборку Docker-образа базы данных с помощью команды:

```Shell
sudo docker compose --file docker_compose/storage.yaml up --build
```

где `docker_compose/storage.yaml` - это имя Docker-образа приложения.

## Сборка Docker-образа через Makefile
Этот проект содержит Makefile, который позволяет легко управлять Docker-контейнерами и запускать ваш сервис.
#### Сборка и запуск контейнера FastAPI
Если вы внесли изменения в код и хотите пересобрать контейнер FastAPI, выполните: `make build-app`
#### Остановка контейнера FastAPI
Для остановки контейнера FastAPI выполните: `make drop-app`
#### Запуск всех контейнеров (FastAPI и MongoDB)
Для одновременного запуска контейнеров FastAPI и MongoDB выполните: `make all`
#### Остановка всех контейнеров
Для остановки всех контейнеров (FastAPI и MongoDB) выполните:`make drop-all`
#### Запуск контейнера MongoDB
Для запуска контейнера MongoDB выполните:`make db`
#### Остановка контейнера MongoDB
Для остановки контейнера MongoDB выполните:`make drop-db`
#### Просмотр логов контейнера FastAPI
Для просмотра логов контейнера FastAPI выполните:`make logs-app`
#### Просмотр логов контейнера MongoDB
Для просмотра логов контейнера MongoDB выполните:`make logs-db`

### Переменные окружения и логгирование

В директории `/core` ожидается `.env` файл со следующими параметрами:

```
DEBUG=(Bool)
URI=(str):(str)
DB=(str)
USER=(str)
PASS=(str)
COLLECTION=(str)
```

где:
`DEBUG` - параметр для включения debug режима (по умолчанию ` false`)
`URI` - аддрес подключения к бд и порт 
`DB` - имя базы данных
`USER` - имя пользователя базы данных
`PASS` - пароль от пользователя
`COLLECTION` - название коллеции


---

В файле `logger.yaml` описаны хендлеры для логирования.
Формат логирования

```yaml
"%(asctime)s [%(filename)s:%(lineno)d] %(levelname)s: %(message)s"
```

Всего реализовано 3 хендлера
`file_handler` - работает на уровне `DEBUG` и записывает логи в файл `my_log.log`
`console_handler` - работает на уровне `INFO` и выводит логи в консоль
`console` - работает на уровне `CRITICAL` и выводит логи в консоль

По умолчанию логгер `debugging` работает на уровне `INFO`

---

В файле `Common/settings.py` находится чтените данных для переменных окружения и логирования

# Пример запроса к POST API

1. Когда сервис запущенн в логах (`make logs-app`) вы получит адресс для перехода к API. По умолчанию адресс `http://localhost:8000`
2. Для удобства рекомендуется использовать `/docs` предоставляемую FastAPI `http://localhost:8000/docs`
3. Вы также можете отправить POST-запрос к сервису с помощью утилиты `curl` или любого другого инструмента для работы с API. Вот пример запроса с использованием `curl`:

```bash
curl -X 'POST' \
  'http://localhost:8000/question/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "question_num":  <INSERT YOUR COUNT>,
}'
```

Этот запрос ваше в качестве `question_num` сервису. В ответ вы получите JSON-ответ с последним вопросом вопросом (если доступно) или `{}` в случае отсутствия ответа.

## Статусы

|Code|Description|Example value|
|---|---|---|
|200|Successful Response|`string`
|422|Validation Error|```json{"detail": [{"loc": ["string",0],"msg": "string","type": "string"}]}```|

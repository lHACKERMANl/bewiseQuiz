DC = docker compose
DCKR = docker
APP_FILE = docker_compose/app.yaml 
DB_FILE = docker_compose/storage.yaml
APP = fastapiapp
DB = mongoContainer
ATTR = 

.PHONY: app
app:
	sudo ${DC} -f ${APP_FILE} up -d

.PHONY: build-app
build-app:
	sudo ${DC} -f ${APP_FILE} up --build -d

.PHONY: drop-app
drop-app:
	sudo ${DC} -f ${APP_FILE} down

.PHONY: all
all:
	sudo ${DC} -f ${APP_FILE} -f ${DB_FILE} up --build -d

.PHONY: drop-all
drop-all:
	sudo ${DC} -f ${APP_FILE} -f ${DB_FILE} down

.PHONY: db
db:
	sudo ${DC} -f ${DB_FILE} up --build -d

.PHONY: drop-db
drop-db:
	sudo ${DC} -f ${DB_FILE} down

.PHONY: logs-app
logs-app:
	sudo ${DCKR} logs ${APP} ${ATTR}

.PHONY: logs-db
logs-db:
	sudo ${DCKR} logs ${DB} ${ATTR}

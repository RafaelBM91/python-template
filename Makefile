build:
	@echo '***BUILD***'
	docker-compose build --force-rm --no-cache --parallel

build-edit:
	@echo '***BUILD-EDIT***'
	docker-compose build --force-rm --parallel

up:
	@echo '***UP***'
	docker-compose up --no-build -d

up-it:
	@echo '***UP-IT***'
	docker-compose up --no-build

down:
	@echo '***DOWN***'
	docker-compose up -d

stop:
	@echo '***STOP***'
	docker-compose stop

delete:
	@echo '***DELETE***'
	docker-compose rm --force

network:
	docker network create codhab-network;

up:
	docker-compose up -d

stop:
	docker-compose up -d

down:
	docker-compose down --volumes

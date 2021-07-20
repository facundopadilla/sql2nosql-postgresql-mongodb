#!make
include docker-environment.env
export
up:
	sudo docker-compose --env-file ./docker-environment.env up --no-build -d
down:
	sudo docker-compose --env-file ./docker-environment.env down
postgres_bash:
	sudo docker exec -it $$POSTGRES_CONTAINER_NAME bash
mongo_bash:
	sudo docker exec -it $$MONGO_CONTAINER_NAME bash
postgres_logs:
	sudo docker logs $$POSTGRES_CONTAINER_NAME
mongo_logs:
	sudo docker logs $$MONGO_CONTAINER_NAME
prune:
	sudo docker builder prune -a -f 
clean:
	sudo docker volume rm -f $$(sudo docker volume ls -q)
	sudo docker system prune -a -f
	sudo docker builder prune --all --force
	sudo apt clean
	sudo apt autoclean
	

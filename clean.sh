docker stop $(docker ps -a -q)
docker volume rm $(docker volume ls -q)
docker rm -vf $(docker ps -aq)
docker rmi -f $(docker images -aq)
docker system prune <<<y

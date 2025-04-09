FROM mysql:latest

COPY vote_system.sql /docker-entrypoint-initdb.d/

ENV MYSQL_DATABASE=vote_db

EXPOSE 3306
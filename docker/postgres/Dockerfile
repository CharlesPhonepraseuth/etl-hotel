FROM library/postgres

WORKDIR /app

COPY ./init.sh /docker-entrypoint-initdb.d
COPY ./db/dump.sql ./db/dump.sql

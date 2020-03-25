# Derived from official mysql image (our base image)
FROM mysql:5.7
# Add a database

EXPOSE 3306

COPY ./CreateTables.sql /docker-entrypoint-initdb.d
# All scripts in docker-entrypoint-initdb.d/ are automatically
# executed during container startup

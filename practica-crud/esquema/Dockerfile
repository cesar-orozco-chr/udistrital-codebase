FROM postgres:13
COPY init.sql /docker-entrypoint-initdb.d
ENV POSTGRES_USER docker
ENV POSTGRES_PASSWORD docker
ENV POSTGRES_DB docker
EXPOSE 5432
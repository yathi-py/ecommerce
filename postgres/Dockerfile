# Use an official PostgreSQL image as a parent image
FROM postgres:latest

# Copy the initialization script into the image
COPY ../init.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL port (not strictly necessary as it's already exposed by the base image)
EXPOSE 5432

# Set the default PostgreSQL user and password
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD password

# Define the default database to be created when the container starts
ENV POSTGRES_DB accounts
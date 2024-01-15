#!/bin/sh

# Function to check if PostgreSQL is ready
wait_for_postgres() {
  until nc -z -v -w30 postgres 5432
  do
    echo "Waiting for PostgreSQL to be ready..."
    sleep 1
  done
}
# Function to check if MongoDB is ready
#wait_for_mongodb() {
#  until nc -z -v -w30 mongodb 27017
#  do
#    echo "Waiting for MongoDB to be ready..."
#    sleep 1
#  done
#}

# Function to apply Django migrations
apply_migrations() {
  python manage.py migrate
  python manage.py migrate products --database mongodb
}

# Function to start Gunicorn server
start_gunicorn() {
  exec gunicorn --bind 0.0.0.0:8000 ecommerce.wsgi:application
}

# Wait for database to be ready
wait_for_postgres
#wait_for_mongodb

# Apply Django migrations
apply_migrations

# Start Gunicorn server
start_gunicorn

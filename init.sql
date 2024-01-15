-- init.sql

-- Create a user with a password
CREATE USER postgres WITH PASSWORD 'password';

-- Grant necessary privileges to the user
ALTER USER postgres CREATEDB;

-- Create a database and set the user as the owner
CREATE DATABASE accounts WITH OWNER = postgres;
GRANT ALL PRIVILEGES ON DATABASE accounts TO postgres;

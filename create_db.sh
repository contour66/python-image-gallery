#!/usr/bin/bash
filename=ig_password
set -e
echo "Creating DB"
psql <<- EOSQL
    CREATE USER image_gallery WITH PASSWORD POSTGRES_PASSWORD_FILE=/run/secrets/ig_password;
    CREATE DATABASE image_gallery;
    GRANT ALL PRIVILEGES ON DATABASE image_gallery TO image_gallery;
EOSQL
echo "Done Creating DB"

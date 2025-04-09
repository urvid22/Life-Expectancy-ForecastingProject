CREATE USER 'urvi_user'@'localhost' IDENTIFIED BY 'serverurd';

CREATE DATABASE life_expectancy_db;

GRANT ALL PRIVILEGES ON life_expectancy_db.* TO 'urvi_user'@'localhost';
FLUSH PRIVILEGES;
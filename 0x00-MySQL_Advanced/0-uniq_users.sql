--creates a table users
--with id, email and name
--Drop the tables if it exists

CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    email CHAR(255) NOT NULL UNIQUE,
    name CHAR(255),
);

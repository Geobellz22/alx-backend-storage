--creates a table users
--with id, email and name
--Drop the tables if it exists
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    PRIMARY KEY (id),
    UNIQUE (email)
);

-- creates the database hbtn_0d_usa and the table states
CREATE DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);

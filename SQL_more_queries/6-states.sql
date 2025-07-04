-- This is a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on the MySQL server.
-- states description:
-- id INT unique, auto generated, cannot be null and is a primary key
-- name VARCHAR(256) cannot be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id)
);

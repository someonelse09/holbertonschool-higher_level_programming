-- This is a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on the MySQL server.
-- cities description:
-- id INT unique, auto generated, cannot be null and is a primary key
-- state_id INT, cannot be null and must be a FOREIGN KEY that references to id of the states table
-- name VARCHAR(256) cannot be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(state_id) REFERENCES states(id)
);

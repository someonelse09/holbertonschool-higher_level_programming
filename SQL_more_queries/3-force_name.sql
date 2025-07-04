-- This is a script that creates the table force_name on MySQL server
-- force_name description:
-- id INT
-- name VARCHAR(256) cannot be null
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
)


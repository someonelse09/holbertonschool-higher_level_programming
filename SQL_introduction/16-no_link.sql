-- This script lists all records of the table second_table of the database hbtn_0c_0 so that rows where the name column does not contain a value is not listed and display the score and the name
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC

-- This is a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0
SELECT score, name FROM second_table
ORDER BY second_table DESC
WHERE score >= 10

-- List records with a score >= 10 in the table second_table ordered by score (top first)
SELECT score, name
FROM hbtn_0c_0.second_table
WHERE score >= 10
ORDER BY score DESC;

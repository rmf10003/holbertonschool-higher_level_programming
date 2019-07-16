-- list num of records with same score in table 
-- use select/count()/as/from/group by
SELECT score, COUNT(score)
AS number
FROM second_table
GROUP BY score DESC;

-- list all record of table second_table
-- use select/from/where/is not null/order by/desc
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

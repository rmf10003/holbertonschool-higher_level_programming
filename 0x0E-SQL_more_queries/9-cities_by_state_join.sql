-- yo
-- yo ma
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_Id = states.id
ORDER BY cities.id;

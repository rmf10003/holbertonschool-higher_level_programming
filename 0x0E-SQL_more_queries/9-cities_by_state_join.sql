-- yo
-- yo ma
SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states
ON cities.state_id = state.id
ORDER BY cities.id;

-- yo
-- yo ma
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.states_id = state.id
ORDER BY cities.id;

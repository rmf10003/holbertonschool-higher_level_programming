-- create table with specs
-- table: unique_id id: unique w/ default name: varchar
CREATE TABLE IF NOT EXISTS unique_id(id INT UNIQUE DEFAULT 1, name VARCHAR(256));

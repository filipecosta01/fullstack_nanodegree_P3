-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament;

\c tournament;

CREATE TABLE players (
  id_player SERIAL PRIMARY KEY,
  name TEXT
);

CREATE TABLE matches (
  id_match SERIAL PRIMARY KEY,
  id_player_one integer REFERENCES players (id_player),
  id_player_two integer REFERENCES players (id_player),
  winner integer REFERENCES players (id_player)
);

\c vagrant;

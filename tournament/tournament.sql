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

CREATE OR REPLACE VIEW results_view AS SELECT p.id_player, p.name,
count (m.winner) as win_num, count(matches_played.id_match) as matches_num
FROM players p LEFT JOIN (
  SELECT p.id_player as id_player, m.id_match
  FROM players p, matches m
  WHERE p.id_player = m.id_player_one
  OR p.id_player = m.id_player_two
) as matches_played ON p.id_player = matches_played.id_player
LEFT JOIN matches as m on p.id_player = m.winner
GROUP BY p.id_player ORDER BY win_num DESC



def playerStandingsQuery():
    """
    Returns:
        A list of tuples, each of which contains (id, name, wins, matches):
          id: the player's unique id (assigned by the database)
          name: the player's full name (as registered)
          wins: the number of matches the player has won
          matches: the number of matches the player has played
    """
    query = ("SELECT p.id_player, p.name, count(p.id_player) as matches_num, "
             "count (m.winner) as win_num "
             "FROM players p LEFT JOIN "
             "(SELECT p.id_player as id_player FROM players p, matches m"
             " WHERE p.id_player = m.id_player_one"
             " OR p.id_player = m.id_player_two "
             ") as matches_played ON p.id_player = matches_played.id_player "
             "LEFT JOIN matches as m on p.id_player = m.winner "
             "GROUP BY p.id_player ORDER BY win_num DESC")
    return query

# select p.id_player, p.name, count(m.winner) as win_num from players as p left join matches as m on p.id_player = m.winner group by p.id_player order by win_num DESC
#select p.id_player, p.name, count(p.id_player) as matches_num from players as p left join (select p.id_player as id_player from players p, matches m where p.id_player = m.id_player_one OR p.id_player = m.id_player_two) as matches_played on p.id_player = matches_played.id_player group by p.id_player


# SELECT p.id_player, p.name, count(p.id_player) as matches_num, count (m.winner) as win_num
# FROM players p LEFT JOIN (SELECT p.id_player as id_player FROM players p, matches m WHERE p.id_player = m.id_player_one OR p.id_player = m.id_player_two) as matches_played on p.id_player = matches_played.id_player
# LEFT JOIN matches as m on p.id_player = m.winner
# GROUP BY p.id_player ORDER BY win_num DESC

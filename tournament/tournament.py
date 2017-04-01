#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

"""
The class represents the tournament itself, connecting/inserting/
creating/retrieving information from database.
"""
class Tournament():
    """
    Class representing the tournament itself.
    """
    def connect(self):
        """
        Connect to the PostgreSQL database.
        Returns a database connection.
        """
        return psycopg2.connect("dbname=tournament")


    def remove_table_records(self, query):
        """
        Remove all the records from the table specified in query from the
        database
        """
        connection = self.connect()

        cursor = connection.cursor()
        cursor.execute(query)

        connection.commit()

        connection.close()


    def insert_table_records(self, query, data):
        """
        Insert into database a new table using the query param, with values from
        data param
        """
        connection = self.connect()

        cursor = connection.cursor()
        cursor.execute(query, data)

        connection.commit()

        connection.close()


    def count_elements(self, query):
        """
        Retrieve the information from database according to the query
        and return a single element with the count of if
        """
        connection = self.connect()

        cursor = connection.cursor()
        cursor.execute(query)

        return cursor.fetchone()[0]

    def select_rows(self, query):
        """
        Select all the rows from the database, according to the query
        """
        connection = self.connect()

        cursor = connection.cursor()
        cursor.execute(query)

        rows = cursor.fetchall()

        return rows


    def delete_matches(self):
        """
        Remove all the match records from the database.
        """
        query = "DELETE FROM matches"
        self.remove_table_records(query)


    def delete_players(self):
        """
        Remove all the player records from the database.
        """
        self.remove_table_records("DELETE FROM players")


    def register_player(self, name):
        """
        Adds a player to the tournament database.

        The database assigns a unique serial id number for the player.  (This
        should be handled by your SQL database schema, not in your Python code.)

        Args:
        name: the player's full name (need not be unique).
        """
        query = "INSERT INTO players (name) VALUES (%s)"
        data = (bleach.clean(name),)
        self.insert_table_records(query, data)


    def count_players(self):
        """
        Returns the number of players currently registered.
        """
        query = "SELECT COUNT(*) FROM players"
        return self.count_elements(query)

    def report_match(self, winner, loser):
        """
        Records the outcome of a single match between two players.

        Args:
        winner:  the id number of the player who won
        loser:  the id number of the player who lost
        """
        statement = ("INSERT INTO matches (id_player_one, id_player_two,"
                     "winner) VALUES (%s, %s, %s)")

        winner = bleach.clean(winner)
        loser = bleach.clean(loser)

        data = (winner, loser, winner)

        self.insert_table_records(statement, data)


    def player_standings(self):
        """
        Returns a list of the players and their win records, sorted by wins.

        The first entry in the list should be the player in first place,
        or a player tied for first place if there is currently a tie.

        Returns:
        A list of tuples, each of which contains (id, name, wins, matches):
            id: the player's unique id (assigned by the database)
            name: the player's full name (as registered)
            wins: the number of matches the player has won
            matches: the number of matches the player has played
        """
        query = "SELECT * FROM results_view"
        return self.select_rows(query)

    def swiss_pairing(self):
        """
        Returns a list of pairs of players for the next round of a match.

        Assuming that there are an even number of players registered,
        each player appears exactly once in the pairings. Each player is paired
        with another player with an equal or nearly-equal win record, that is,
        a player adjacent to him or her in the standings.

        Returns:
        A list of tuples, each of which contains (id1, name1, id2, name2)
            id1: the first player's unique id
            name1: the first player's name
            id2: the second player's unique id
            name2: the second player's name
        """
        query = "SELECT * FROM results_view"
        rows = self.select_rows(query)

        """
        The results array will be formed by:
            1. As the player standings query return the elements already sorted
               by the number of wins descendant (higher number of victories 1st)
               we can pair two sequencial rows to be returned in a tuple
            2. The zip function gets all the rows and pair them two by two and
               return the values paired to player_one and player_two until the
               end of the array.
            3. The results variable is now a tuple of players that will play
               agains each other.
        """
        results = [(player_one[0], player_one[1], player_two[0], player_two[1])
                   for player_one, player_two in zip(rows, rows[1:])[::2]]
        return results

# Create a new tornament to be used inside the functions below
tournament = Tournament()


"""
All those below are test functions are due to the test file, I won't fix the
pep8 issue with the name of the function.
"""
def deleteMatches():
    """Remove all the match records from the database."""
    tournament.delete_matches()


def deletePlayers():
    """Remove all the player records from the database."""
    tournament.delete_players()


def countPlayers():
    """
    Returns the number of players currently registered.
    """
    return tournament.count_players()


def registerPlayer(name):
    """
    Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    tournament.register_player(name)


def playerStandings():
    """
    Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    return tournament.player_standings()


def reportMatch(winner, loser):
    """
    Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    tournament.report_match(winner, loser)


def swissPairings():
    """
    Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings. Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    return tournament.swiss_pairing()



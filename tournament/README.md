Udacity - Tournament Results - Project 3 - Filipe Costa
============

This is a python project intended to simulate a tournament swiss-paringin type,
store data about the tournament using PostgreSQL.

## Libraries
This project uses external library other than the ones included in
Python Source Libraries. They are:
1. psycopg2
2. bleach

Make sure you have them installed before moving forward.

## Demo
(MacOS instructions) You can run the tests following these steps (after cloning):
1. Install [Python](https://www.python.org/)
2. Open a terminal and check Python is installed and running properly
   1. You can try 'python --version' in terminal and check the output
3. Go to `tournament` folder
4. Run the database and tables creation by doing:
   1. Install [PostgreSQL](http://exponential.io/blog/2015/02/21/install-postgresql-on-mac-os-x-via-brew/)
   2. From the terminal, run the command `psql`
   3. Run the command `\i tournament.sql` to create the database and tables automatically.
   Do not move forward until this step is done.
   4. Open a new terminal and run `python  tournament_test.py`
5. Verify the message 'Success!  All tests pass!' on your terminal 

## Important information
Vagrant files are included just for creating a new virtual machine to run the project.
If you feel like using it, please read [Vagrant Documentation]() first.
Then, from the root folder of the project, run `vagrant up` to install all the dependencies and mount the new virtual
machine.

## [Contacting the Author](mailto:s.costa.filipe@gmail.com)
Click above and feel free to get in touch in case of trouble or suggestions.
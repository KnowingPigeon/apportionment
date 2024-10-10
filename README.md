# Apportionment algorithm

This project allows for the apportionment of hypothetical U.S. House of Representatives-style legislatures based on primary division populations.
For example, under the current apportionment the State of Washington has 10 representatives in Congress. But what if we increased Washington's population
by a few million? Added new states? This project intends to easily answer such questions.

## Usage

Any apportionment necessitates at least one CSV file containing a list of tuples containing a state name, abbreviation, and population. huntington-hill.py's apportion() can be
passed a list of these CSV files (or more accurately the names of these CSV files) and a number of seats to apportion. A file of the form 
"[CSV file name 1]+[CSV file name 2]+...+[CSV file name n]<number of seats>.txt" will be outputted to bin, including a list of state names and the number of seats each is
apportioned.

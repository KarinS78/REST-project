class Flights:
    def __init__(self, flight_id, timestamp, remaining_seats, origin_country_id, dest_country_id):
        self.flight_id = flight_id
        self.timestamp = timestamp
        self.remaining_seats = remaining_seats
        self.origin_country_id = origin_country_id
        self.dest_country_id = dest_country_id

    def __repr__(self):
        return f'\'flight_id\':{self.flight_id},\'time_stamp\': {self.timestamp}, \'remaining_seats\':{self.remaining_seats}, \'origin_country_id\':{self.origin_country_id}, \'dest_country_id\':{self.dest_country_id}) '


import sqlite3

conn = sqlite3.connect(r'C:\Users\eliav\Desktop\קורס\final_project.db')


# this function prints all the flights there are on the table with the given condition.
def print_fli(cond=''):
    flights = conn.execute(f'SELECT * FROM flights {cond}')
    lst = []
    for flight in flights:
        temp = Flights(flight[0], flight[1], flight[2], flight[3], flight[4])
        lst.append([temp])
    return lst


# this function inserts a  given flight to the table.
def insert_fli(flight):
    conn.execute(
        f'INSERT INTO flights(timestamp, origin_country_id, dest_country_id) VALUES({flight.timestamp},{flight.origin_country_id},{flight.dest_country_id})')
    conn.commit()


# this function updates a given flight according to a given values.
def update_fli(flight):
    conn.execute(
        f'UPDATE flights SET timestamp = {flight.timestamp}, origin_country_id = {flight.origin_country_id}, dest_country_id = {flight.dest_country_id} WHERE flight_id = {flight.flight_id}')
    conn.commit()


# this function delete a given flight from the table.
def delete_fli(flight_id):
    conn.execute(f'DELETE FROM flights WHERE flight_id = {flight_id}')
    conn.commit()


conn.close()

class Tickets:
    def __init__(self, ticket_id, user_id, flight_id):
        self.ticket_id = ticket_id
        self.user_id = user_id
        self.flight_id = flight_id

    def __repr__(self):
        return f'\'ticket_id\':{self.ticket_id}, \'user_id\':{self.user_id},\'flight_id\': {self.flight_id})'


import sqlite3

conn = sqlite3.connect(r'C:\Users\eliav\Desktop\קורס\final_project.db')


# this function prints all the tickets there are on the table with the given condition.
def print_tic(cond=''):
    tickets = conn.execute(f'SELECT * FROM tickets {cond}')
    lst = []
    for ticket in tickets:
        temp = Tickets(ticket[0], ticket[1], ticket[2])
        lst.append({temp})
    return lst


# this function deletes the ticket with the given ticket id.
def delete_tic(id):
    flight_id = conn.execute(f'SELECT flight_id FROM flights WHERE ticket_id = {id}')
    conn.execute(f'DELETE FROM tickets WHERE ticket_id  = {id}')
    conn.commit()
    conn.execute(f'UPDATE flights set remaining_seats = (SELECT remaining_seats FROM flights WHERE flight_id = {flight_id}) +1')
    conn.commit()


# this given function inserts a ticket with the given values.
def insert_tic(ticket):
    conn.execute(f'INSERT INTO tickets (user_id, flight_id) VALUES ({ticket.user_id},{ticket.flight_id})')
    conn.commit()
    conn.execute(f'UPDATE flights set remaining_seats = (SELECT remaining_seats FROM flights WHERE flight_id = {ticket.flight_id}) -1')
    conn.commit()


conn.close()

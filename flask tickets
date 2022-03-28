from flask import Flask
import tickets
from flask import render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/form/tickets', methods=['GET'])
def form():
    return render_template('theTicketSite.html')


@app.route('/tickets', methods=['GET', 'POST'])
def tickets_page():
    # request for all the tickets
    if request.method == 'GET':
        return tickets.print_tic()
    # request to create a new ticket
    if request.method == 'POST':
        ticket_id = request.form['ticket id']
        flight_id = request.form['flight id']
        user_id = request.form['user id']
        ticket = tickets.Tickets(ticket_id, flight_id, user_id)
        return tickets.insert_tic(ticket)


@app.route('/tickets/<int:ticket_id>', methods=['GET', 'DELETE'])
def ticket_g_d(ticket_id):
    # request of a specific ticket
    if request.method == 'GET':
        return tickets.print_tic(f'WHERE ticket_id = {ticket_id}')
    # request to delete a ticket according to a given id
    if request.method == 'DELETE':
        return tickets.delete_tic(ticket_id)


app.run()

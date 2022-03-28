from flask import Flask
import flights
from flask import render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/form/flights', methods=['GET'])
def form():
    return render_template('theFlightSite.html')


@app.route('/flights', methods=['GET', 'POST'])
def flights_page():
    # request for all the flights
    if request.method == 'GET':
        return flights.print_fli()
    # request to create a new flight
    if request.method == 'POST':
        flight_id = request.form['id']
        timestamp = request.form['time']
        remaining_seats = request.form['remaining seats']
        origin_country_id = request.form['original country id']
        dest_country_id = request.form['destination country id']
        flight = flights.Flights(flight_id, timestamp, remaining_seats, origin_country_id, dest_country_id)
        return flights.insert_fli(flight)


@app.route('/flights/<int:flight_id>', methods=['GET', 'DELETE'])
def flights_g_d(flight_id):
    # request of a specific flight
    if request.method == 'GET':
        return flights.print_fli(f'WHERE code_AI = {flight_id}')
    # request to delete a flight according to a given id
    if request.method == 'DELETE':
        return flights.delete_fli(flight_id)


@app.route('/flights/put', methods=['PUT'])
def flights_put():
    # request to update a flight that's already exist
    if request.method == 'PUT':
        flight_id = request.form['id']
        timestamp = request.form['time']
        remaining_seats = request.form['remaining seats']
        origin_country_id = request.form['original country id']
        dest_country_id = request.form['destination country id']
        flight = flights.Flights(flight_id, timestamp, remaining_seats, origin_country_id, dest_country_id)
        return flights.update_fli(flight)


app.run()

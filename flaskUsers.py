from flask import Flask
from flask import render_template, request, redirect, url_for
import users

app = Flask(__name__)


@app.route('/users_home', methods=['GET'])
def form():
    return render_template('theUsersSite.html')


@app.route('/users', methods=['GET', 'POST'])
def users_page():
    # request for all the users
    if request.method == 'GET':
        print(users.print_users())
        return render_template('theTicketSite.html')
    # request to create a new user
    if request.method == 'POST':
        full_name = request.form['full name']
        password = request.form['psw']
        real_id = request.form['id']
        user = users.Users(0, full_name, password, real_id)
        users.insert_user(user)
        return render_template('theTicketSite.html')


@app.route('/users/<int:user_id>', methods=['GET', 'DELETE'])
def user_g_d(user_id):
    # request of a specific user
    if request.method == 'GET':
        return users.print_users(f'WHERE user_id = {user_id}')
    # request to delete a user according to a given id
    if request.method == 'DELETE':
        return users.delete_user(user_id)


@app.route('/users/put', methods=['PUT'])
def users_put():
    # request to update a user that's already exist
    full_name = request.form['full name']
    password = request.form['psw']
    real_id = request.form['id']
    user = users.User(0, full_name, password, real_id)
    return users.update_user(user)


app.run()

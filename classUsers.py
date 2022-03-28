class Users:
    def __init__(self, id_AI, full_name, password, real_id):
        self.id_AI = id_AI
        self.full_name = full_name
        self.password = password
        self.real_id = real_id

    def __repr__(self):
        return f'\'id_AI\':{self.id_AI},\'full_name\':\'{self.full_name}\',\'password\': \'{self.password}\', \'real_d\':\'{self.real_id}\')'


import sqlite3

conn = sqlite3.connect(r'C:\Users\eliav\Desktop\קורס\final_project.db')


# this function prints all the users there are on the table with the given condition.
def print_users(cond=''):
    users = conn.execute(f'SELECT * FROM users {cond}')

    lst = []
    for user in users:
        temp = Users(user[0], user[1], user[2], user[3])
        lst.append({temp})
    return lst


# this function inserts a  given user to the table.
def insert_user(user):
    conn.execute(
        f'INSERT INTO users (full_name, password, real_id) VALUES ("{user.full_name}","{user.password}","{user.real_id}")')
    conn.commit()


# this function update a user according to a given values.
def update_user(user):
    id_AI = f'SELECT id_AI FROM users WHERE real_id = "{user.real_id}'
    conn.execute(
        f'UPDATE users SET full_name = "{user.full_name}", password = "{user.password}", real_id = "{user.real_id}" WHERE id_AI = {id_AI}')
    conn.commit()


# this function deletes a user according to a given id.
def delete_user(id):
    conn.execute(f'DELETE FROM users WHERE  id_AI = {id}')
    conn.commit()


conn.close()

import sqlite3
# Query Str
CREATE_TABLE_USERS = "CREATE TABLE IF NOT EXISTS tbl_users (users_id INTEGER PRIMARY KEY AUTOINCREMENT , name TEXT NOT NULL , lastname TEXT NOT NULL , username TEXT NOT NULL\
                      , password INTEGER NOT NULL , email TEXT NOT NULL DEFAULT '' , age INTEGER NOT NULL DEFAULT '' , gender TEXT NOT NULL DEFAULT '' , country TEXT NOT NULL DEFAULT '' , city TEXT NOT NULL DEFAULT '' , phone_number TEXT NOT NULL DEFAULT '')"
CREATE_TABLE_CHAT_CONTACT1 = "CREATE TABLE IF NOT EXISTS tbl_chat1 (chat_id INTEGER PRIMARY KEY AUTOINCREMENT , chat_user TEXT, chat_contact TEXT, user_id INTEGER)"
CREATE_TABLE_CHAT_CONTACT2 = "CREATE TABLE IF NOT EXISTS tbl_chat2 (chat_id INTEGER PRIMARY KEY AUTOINCREMENT , chat_user TEXT, chat_contact TEXT, user_id INTEGER)"
INSERT_INTO_CHAT_CONTACT1 = "INSERT INTO tbl_chat1 (chat_user , chat_contact , user_id) VALUES (?,?,?)"
INSERT_INTO_CHAT_CONTACT2 = "INSERT INTO tbl_chat2 (chat_user , chat_contact , user_id) VALUES (?,?,?)"
SELECT_CHAT_CONTACT1 = "SELECT chat_user , chat_contact FROM tbl_chat1 WHERE user_id = ?"
SELECT_CHAT_CONTACT2 = "SELECT chat_user , chat_contact FROM tbl_chat2 WHERE user_id = ?"
INSERT_INTO_USERS = "INSERT INTO tbl_users (name , lastname , username , password) VALUES (?,?,?,?)"
CHECK_LOGIN = "SELECT * FROM tbl_users WHERE username = ? AND password = ?"
UPDATE_USER_INFORMATION = "UPDATE tbl_users SET email = ? , age = ? , gender = ? , country = ? , city = ? , phone_number = ? WHERE username = ? AND password = ?"
USERNAME_CHECK = "SELECT * FROM tbl_users WHERE username = ?"
# Connect Method
def check_connection():
    connection = sqlite3.connect("chatroom.db")
    return connection
# Query Method
def create_table_users(connection):
    with connection:
        connection.execute(CREATE_TABLE_USERS)
def create_table_chat_contact1(connection):
    with connection:
        connection.execute(CREATE_TABLE_CHAT_CONTACT1)
def create_table_chat_contact2(connection):
    with connection:
        connection.execute(CREATE_TABLE_CHAT_CONTACT2)
def insert_into_chat1(connection , chat_user , chat_contact , user_id):
    with connection:
        connection.execute(INSERT_INTO_CHAT_CONTACT1 , (chat_user , chat_contact , user_id))
def insert_into_chat2(connection , chat_user , chat_contact , user_id):
    with connection:
        connection.execute(INSERT_INTO_CHAT_CONTACT2 , (chat_user , chat_contact , user_id))
def select_chat_contact1(connection , user_id):
    with connection:
        return connection.execute(SELECT_CHAT_CONTACT1 , (user_id ,)).fetchall()
def select_chat_contact2(connection , user_id):
    with connection:
        return connection.execute(SELECT_CHAT_CONTACT2 , (user_id ,)).fetchall()
def insert_into_users(connection , name , lastname , username , password):
    with connection:
        connection.execute(INSERT_INTO_USERS , (name , lastname , username , password))
def check_login(connection , username , password):
    with connection:
        return connection.execute(CHECK_LOGIN , (username , password)).fetchall()
def update_user_information(connection , email , age , gender , country , city , phone_number , username , password):
    with connection:
        connection.execute(UPDATE_USER_INFORMATION , (email , age , gender , country , city , phone_number , username , password))
def username_check(connection , username):
    with connection:
        return connection.execute(USERNAME_CHECK , (username ,)).fetchall()
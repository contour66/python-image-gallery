import psycopg2
import json
import os
from .secrets import get_secret_image_gallery

connection = None


def get_secret():
    jsonString = get_secret_image_gallery()
    return json.loads(jsonString)


def get_password(secret):
    if secret:
        os.environ["IG_PASSWORD"] = secret
    return secret['password']


def get_host(secret):
    if secret:
        os.environ["IG_HOST"] = secret
    return secret['host']


def get_username(secret):
    if secret:
        os.environ["IG_USERNAME"] = secret
    return secret['username']


def get_full_name(secret):
    if secret:
        os.environ["IG_FULL_NAME"] = secret
    return secret['full_name']


def get_dbname(secret):
    if secret:
        os.environ["IG_DATABASE"] = secret
    return secret['dbname']


def connect():
    global connection
    secret = get_secret()
    connection = psycopg2.connect(host=get_host(secret), dbname=get_dbname(secret), user=get_username(secret),
                                  password=get_password(secret))


def execute(query, args=None):
    global connection
    cursor = connection.cursor()
    if not args:
        cursor.execute(query)
    else:
        cursor.execute(query, args)
    return cursor


def print_names():
    try:
        connect()
        cursor = connection.cursor()
        cursor.execute('select username from users;')
        res = cursor.fetchall()
        print(res)
        return res
    finally:
        connection.close()


def delete_user_ui(username):
    try:
        connect()
        cursor = connection.cursor()
        connection.set_session(autocommit=True)
        cursor.execute('delete from users where username = %s', (username,))
        print("\nDeleted\n" + username)
    finally:
        connection.close()


def username_exists(username):
    try:
        exists_query = '''
        select exists (
            select 1
            from users
            where username = %s
        )'''
        connect()
        cursor = connection.cursor()
        cursor.execute(exists_query, (username,))
        return cursor.fetchone()[0]
    finally:
        connection.close()


def User(username, password, full_name):
    username = username
    password = password
    full_name = full_name


def get_current_user(name):
    return


def get_user_pw(username):
    try:
        connect()
        cursor = connection.cursor()
        cursor.execute('select username, password, full_name from users where username = %s', (username,))
        row = cursor.fetchone()
        if row is None:
            return None
        else:
            return row[1]
    finally:
        connection.close()


def add_user_ui(username, password, fullname):
    try:
        connect()
        cursor = connection.cursor()
        connection.set_session(autocommit=True)
        execute("""insert into users (username, password, full_name) values(%s, %s, %s); """,
                (username, password, fullname))
        print('\nUser: ' + username + '\nPassword: ' + password + '\nFull name: ' + ' added to table users\n')

    finally:
        connection.close()


# EDITS USER IN TABLE ////////////
def edit_user_ui(username, password, fullname):
    try:
        connect()
        cursor = connection.cursor()
        connection.set_session(autocommit=True)
        if password:
            execute("update users set password=%s where username=%s", (password, username,))
            print("\nPassword updated\n")
        if fullname:
            execute("update users set full_name=%s where username=%s", (fullname, username,))
            print("\nName updated\n")
    finally:
        connection.close()


def main():
    print("name")


if __name__ == '__main__':
    main()
# def get_name(username):e
#     res = execute('select from users where username;')
#     for row in res:
#         print(row)

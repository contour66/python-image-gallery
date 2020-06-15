import psycopg2
import json
from secrets import get_secret_image_gallery
from db import

connection = None


def get_secret():
    jsonString = get_secret_image_gallery()
    return json.loads(jsonString)


def get_password(secret):
    return secret['password']


def get_host(secret):
    return secret['host']


def get_username(secret):
    return secret['username']


def get_full_name(secret):
    return secret['full_name']


def get_dbname(secret):
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
    connect()
    cursor = connection.cursor()
    cursor.execute('select username from users;')
    res = cursor.fetchall()
    print(res)

    return res

def delete_user_ui(user):
    execute("delete from users where username = %s", (user,))
    connect()
    cursor = connection.cursor()
    cursor.execute('select username from users;')
    res = cursor.fetchall()
    print(res)


def delete_user():
    print('Enter username to delete:')
    user = input()
    print('\nAre you sure that you want to delete [ ' + user + ' ]?')
    delete = input()
    if username_exists(user):
        if delete == 'yes':
            execute("delete from users where username = %s", (user,))
            print("\nDeleted\n")
    else:
        print("\nNo such user exists\n")


# 	row = cursor.fetchone()
# print(row)


def main():
    connect()
    res = execute('select * from users;')
    for row in res:
        print(row)


if __name__ == '__main__':
    main()

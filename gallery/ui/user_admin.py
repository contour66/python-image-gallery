import psycopg2
import json
from .secrets import get_secret_image_gallery

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


# PRINTS MAIN MENU /////////////////////
def ask_user():
    print('''
        1) List users
        2) Add user
        3) Edit user
        4) Delete user
        5) Quit ''')


# PRINTS THE NAMES /////////////////////
def print_names():
    res = execute('select * from users;')
    for row in res:
        print(row)


# CHECKS IF USER EXISTS IN TABLE //////
def username_exists(username):
    exists_query = '''
        select exists (
            select 1
            from users
            where username = %s
        )'''
    cursor = connection.cursor()
    cursor.execute(exists_query, (username,))
    return cursor.fetchone()[0]


# ADDS A USER TO THE TABLE ////////////
def add_user():
    print('Enter username:')
    user = input()
    print('Enter password:')
    pw = input()
    print('Enter name:')
    name = input()
    # res = execute("""select exists (select 1 from users where username) valies(%s)""", user)
    if username_exists(user):
        print("\nError: user with username " + user + " already exists\n")
    else:
        execute("""insert into users (username, password, full_name) values(%s, %s, %s); """, (user, pw, name))
        print('\nUser ' + name + ' added to table users\n')
        print_names()


# DELETES USER IN TABLE /////////////
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


# EDITS USER IN TABLE ////////////
def edit_user():
    print('Enter username to edit:')
    user = input()
    if username_exists(user):
        print('New password (press enter to keep current):')
        pw = input()
        print('New full name (press enter to keep current):')
        name = input()
        if pw:
            execute("update users set password=%s where username=%s", (pw, user,))
            print("\nPassword updated\n")
        if name:
            execute("update users set full_name=%s where username=%s", (name, user,))
            print("\nName updated\n")
    else:
        print("\nNo such user exists\n")


def main():
    try:
        connect()
        connection.set_session(autocommit=True)
        while True:
            ask_user()
            choice = int(input())
            if choice == 1:
                print_names()
            elif choice == 2:
                add_user()
            elif choice == 3:
                edit_user()
            elif choice == 6:
                username_exists("dog")
            elif choice == 4:
                delete_user()
            elif choice == 5:
                print("\n Quitting program")
                break
            else:
                print("Invalid")
    finally:
        connection.close()

    # res = execute("update users set password=%s where username='fred'", ('banana',))
    # res = execute('select * from users;')


if __name__ == '__main__':
    main()

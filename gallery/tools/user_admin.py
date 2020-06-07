import psycopg2

db_host = "demo-databsae-2.cfxeylolmgaa.us-west-1.rds.amazonaws.com"
db_name = "image_gallery"
db_user = "image_gallery"

password_file = "/home/ec2-user/.image_gallery_config"
connection = None


def get_password():
    f = open(password_file, "r")
    result = f.readline()
    f.close()
    return result[:-1]


def connect():
    global connection
    connection = psycopg2.connect(host=db_host, dbname=db_name, user=db_user,
                                  password=get_password())


def execute(query, args=None):
    global connection
    cursor = connection.cursor()
    if not args:
        cursor.execute(query)
    else:
        cursor.execute(query, args)
    return cursor


def ask_user():
    print('''
        1) List users
        2) Add user
        3) Edit user
        4) Delete user
        5) Quit ''')

# PRINTS THE NAMES ////////////////////

def print_names():
    res = execute('select * from users;')
    for row in res:
        print(row)



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


def edit_user():
    print('Enter username to edit:')
    user = input()
    if username_exists(user):
        print('New password (press enter to keep current):')
        pw = input()
        print('New full name (press enter to keep current):')
        name = input()
        if pw:
            execute("update users set password=%s where username=%s", (pw,))
            print("\nPassword updated\n")
        if name:
            execute("update users set name=%s where username=%s", (name,))
            print("\nName updated\n")
    else:
        print("\nNo such user exists\n")


def main():
    connect()

    while True:
        ask_user()
        choice = int(input())
        if choice == 1:
            print_names()
        elif choice == 2:
            add_user()
        elif choice == 3:
            edit_user()
        elif choice == 4:
            delete_user()
        elif choice == 5:
            print("\n Quitting program")
            break
        else:
            print("Invalid")

    # res = execute("update users set password=%s where username='fred'", ('banana',))
    # res = execute('select * from users;')


if __name__ == '__main__':
    main()

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


# ADDS A USER TO THE TABLE ////////////

def add_user():
    print('Enter username:')
    user = input()
    print('Enter password:')
    pw = input()
    print('Enter name:')
    name = input()
    res = execute("""select exists (select 1 from users where username) valies(%s)""", user)
    if res == 0:
        execute("""insert into users (username, password, full_name) values(%s, %s, %s); """, (user, pw, name))
        print('\nUser ' + name + ' added to table users\n')
    else:
        print("Username " + user + " already exists")

def main():
    connect()

    while True:
        ask_user()
        choice = int(input())
        if choice == 1:
            print_names()
        elif choice == 2:
            add_user()
            print_names()
        elif choice == 5:
            print("\n Quitting program")
            break
        else:
            print("Invalid")

    # res = execute("update users set password=%s where username='fred'", ('banana',))
    # res = execute('select * from users;')


if __name__ == '__main__':
    main()

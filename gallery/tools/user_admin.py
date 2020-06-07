

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


# def query_action(arg):
#       switcher = {
#       1: print_names()
#        func = switcher.get(arg)
#       return func()

# PRINTS THE NAMES ////////////////////

def print_names():
    res = execute('select * from users;')
    for row in res:
        print(row)

# ADDS A USER TO THE TABLE ////////////

def add_user(user, pw, name):
	res = execute("insert into users values (user, pw, name)")
	
def main():
    connect()
    ask_user()
    choice = input()
    if choice == 1:
        print_names()
    if choice == 2:
        print('Enter username:' )
        user = input()
        print('Enter password:' )
        pw = input()
        print('Enter name:' )
        name = input()
	add_user(user, pw, name)
	pw = input()
	print('User ' + name + 'added')
	print_names()
    res = execute('select * from users;')
    for row in res:
        print(row)
    res = execute("update users set password=%s where username='fred'", ('banana',))
    res = execute('select * from users;')
    for row in res:
        print(row)


if __name__ == '__main__':
   main()

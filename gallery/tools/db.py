import psycopg2
import json
from secrets import get_secret_image_gallery()

db_host = "image-gallery.cfxeylolmgaa.us-west-1.rds.amazonaws.com"
db_name = "image_gallery"
db_user = "image_gallery"

password_file = "/home/ec2-user/.image_gallery_config"
connection = None

def get_secret():
	f = open(password_file, "r")
	result = f.readline()
	f.close()
	return result[:-2]

def connect():
	global connection
	connection = psycopg2.connect(host=db_host, dbname=db_name, user=db_user, password=get_password())

def execute(query, args=None):
	global connection	
	cursor = connection.cursor()
	if not args:
		cursor.execute(query)
	else:
		cursor.execute(query, args)	
	return cursor	

def main():
	connect()
	res = execute('select * from users;')
	for row in res:
		print(row)
	res = execute("update users set password=%s where username='fred'",('banana',))
	res = execute('select * from users;')
	for row in res:
                print(row)


if __name__ =='__main__':
	main()

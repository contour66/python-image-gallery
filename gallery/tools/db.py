import psycopg2
import json
from secrets import get_secret_image_gallery()

db_host = "image-gallery.cfxeylolmgaa.us-west-1.rds.amazonaws.com"
db_name = "image_gallery"
db_user = "image_gallery"

connection = None

def get_secret():
	jsonString = get_secret_image_gallery()
	return json.loads(jsonString)

def get_password(secret):
	return secret['password']

def get_host(secret):
	return secret['host']

def get_username(secret):
	return secret['host']

def get_full_name(secret):
	return secret['full_name']


def connect():
	global connection
	secret = get_secret()
	connection = psycopg2.connect(host=get_host(secret), dbname=db_name, user=get_username(secret), password=get_password(secret))

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


if __name__ =='__main__':
	main()

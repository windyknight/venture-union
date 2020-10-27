import psycopg2

con = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="localhost",port="5432")
con.autocommit=True

cur = con.cursor()

print("Connected to PostgreSQL")

try:
	cur.execute("SELECT * FROM item")
	cur.fetchall()
	#raise Exception() #debug code!!!! DO NOT UNCOMMENT THIS LINE!!!
except: #database absent, create it
	try:
		print('Recreating database...')
		commands = open('main.sql').read().split('\n')
		commands = ''.join(commands)
		commands = commands.split(';')
		for i in commands:
			cur.execute(i+';')
	except:
		print(i)
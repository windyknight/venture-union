import psycopg2

con = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="localhost",port="5432")

cur = con.cursor()

print("Connected to PostgreSQL")
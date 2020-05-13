#!/usr/bin/python3
import configparser
import pymysql.cursors
import queries 

Config = configparser.ConfigParser()
Config.read('backup.cnf')
client = dict(Config.items('client'))

# Connect to the database
connection = pymysql.connect( client['host'], client['user'], client['password'], 'foodlog')

try:
  with connection.cursor() as cursor:
    cursor.execute(queries.selUsers)
    result = cursor.fetchall()
    print(result)
finally:
  connection.close()
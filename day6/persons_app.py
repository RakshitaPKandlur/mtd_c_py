import pymysql

def connect_db():
    connection = pymysql.Connect(host = 'localhost', user = 'root', password = 'root', database = 'rakshita_db', charset = 'utf8', port = 3306)
    print('DB Connected')
    return connection

def disconnect_db(connection):
    connection.close()
    print('DB Dis - Connected')

def create_db():
    query = 'create database IF NOT EXISTS rakshita_db '
    connection =  connect_db()
    cursor = connection.cursor()
    cursor.execute(query, object)
    connection.commit()
    cursor.close()
    disconnect_db(connection)

def run_query(query, object = None):
    connection =  connect_db()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    disconnect_db(connection)

def create_table():
    query = 'create table employees(id int primary key auto_increment, name varchar(40) not null, designation varchar(30), phone_number bigint unique, salary float, commission float default(0))'
    run_query(query)

def read_person_details():
    name = input('Enter the person name: ')
    location = input('Enter the person location: ')
    gender = ('Enter the person gender: ')
    return(name, gender, location)

def insert_person():
    person = read_person_details()
    query = 'insert into persons(name, gender, location) values(%s, %s, %s);'
    run_query(query, person)

insert_person()

def delete_person():
    id = int(input('Enter '))

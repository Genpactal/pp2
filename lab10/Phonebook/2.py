import psycopg2
import csv

def insert_data_from_csv(file):
    conn = psycopg2.connect(
        host='localhost',
        database='phone',
        user='postgres',
        password='6618',
    )
    conn.autocommit = True

    cursor = conn.cursor()

    with open(file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            cursor.execute(
                "INSERT INTO PhoneBook (first_name, last_name, phone_num) VALUES (%s, %s, %s)",
                (row[0], row[1], row[2])
            )

    conn.close()

file='contacts.csv'
insert_data_from_csv(file)
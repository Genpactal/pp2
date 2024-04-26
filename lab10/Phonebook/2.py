import psycopg2
import csv

def insert_data_from_csv(file_path):
    conn = psycopg2.connect(
        host='localhost',
        database='phone',
        user='user',
        password='12345',
        port='54321'
    )
    conn.autocommit = True

    cursor = conn.cursor()

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            cursor.execute(
                "INSERT INTO PhoneBook (first_name, last_name, phone_num) VALUES (%s, %s, %s)",
                (row[0], row[1], row[2])
            )

    conn.close()

insert_data_from_csv('contacts.csv')
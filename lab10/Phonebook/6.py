import psycopg2

def delete_contact_by_username(first_name):
    conn = psycopg2.connect(
        host='localhost',
        database='phone',
        user='postgres',
        password='6618',
    )
    conn.autocommit = True

    cursor = conn.cursor()

    cursor.execute("DELETE FROM PhoneBook WHERE first_name = %s", (first_name,))

    conn.close()

def delete_contact_by_phone(phone_num):
    conn = psycopg2.connect(
        host='localhost',
        database='phone',
        user='user',
        password='12345',
        port='54321'
    )
    conn.autocommit = True

    cursor = conn.cursor()

    cursor.execute("DELETE FROM PhoneBook WHERE phone_num = %s", (phone_num,))

    conn.close()

delete_contact_by_username('John')
delete_contact_by_phone('1234567890')
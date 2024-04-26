import psycopg2

def update_contact(first_name, new_phone_num):
    conn = psycopg2.connect(
        host='localhost',
        database='phone',
        user='user',
        password='12345',
        port='54321'
    )
    conn.autocommit = True

    cursor = conn.cursor()

    cursor.execute(
        "UPDATE PhoneBook SET phone_num = %s WHERE first_name = %s",
        (new_phone_num, first_name)
    )

    conn.close()

update_contact('John', '1234567890')
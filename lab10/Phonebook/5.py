import psycopg2

def query_contacts(last_name=None):
    conn = psycopg2.connect(
        host='localhost',
        database='phone',
        user='postgres',
        password='6618',
    )
    conn.autocommit = True

    cursor = conn.cursor()

    if last_name:
        cursor.execute("SELECT * FROM PhoneBook WHERE last_name = %s", (last_name,))
    else:
        cursor.execute("SELECT * FROM PhoneBook")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

query_contacts()  # Fetch all contacts
query_contacts('Doe')  # Fetch contacts with last name 'Doe'
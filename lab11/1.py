import psycopg2

conn = psycopg2.connect(
	database="postgres",
	user='postgres',
	password='6618',
	host='localhost'
)
''' create or replace function getPhone(name varchar)
               returns setof Phonebook
       as
       $$
       begin
          return query
          select *  from Phonebook
          where (Phonebook.first_name = $1) or (Phonebook.last_name = $1);
       end
       $$
       language plpgsql;'''


cursor = conn.cursor()
conn.autocommit = True

name = str(input("name: "))
cursor.callproc('getPhone', [name])
result = cursor.fetchall()
print(result)
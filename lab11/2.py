import psycopg2

conn = psycopg2.connect(
	database="postgres",
	user='postgres',
	password='6618',
	host='localhost',
)

'''create or replace procedure addPhone(first_name varchar, last_name varchar, phone_number varchar)
        as
        $$
        begin
           update Phonebook
           set phone_number = $3
           where (Phonebook.first_name = $1) and (Phonebook.last_name = $2);
           IF NOT FOUND THEN
           insert into phonebook(first_name,last_name,phone_number) values ($1, $2, $3);
          END IF;
        end;
        $$
    LANGUAGE plpgsql;'''

cursor = conn.cursor()
conn.autocommit = True
first_name = str(input("First_name: "))
last_name = str(input("Last_name: "))
num= str(input("Num: "))


cursor.execute('CALL addPhone(%s,%s,%s)', (first_name, last_name, num))



cursor.callproc('getPhone', [first_name])
result = cursor.fetchall()
print(result)
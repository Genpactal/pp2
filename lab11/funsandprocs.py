import psycopg2
from config import load_config

def create_func():
    """ Create functions in the PostgreSQL database"""
    commands = (
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
       language plpgsql;''',
       
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
    LANGUAGE plpgsql;''',
    
   ''' create or replace function getAllPhone(lim integer, ofs integer )
       returns setof Phonebook
        as
        $$
        begin
           return query
           select * from Phonebook limit $1 offset $2;
        end;  
        $$ language plpgsql;
        select *
        from getAllPhone(1,2);'''
        )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_func()
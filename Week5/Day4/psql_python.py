import psycopg2
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'MMBmmb_11'
DATABASE = 'Hollywood'

connection = psycopg2.connect(host = HOSTNAME, user = USERNAME, password=PASSWORD, dbname = DATABASE)

def run_select_query(query: str):

    with connection.cursor() as cursor:
        # cursor - query runner
        cursor.execute(query)
        # cursor.fetchall returns all data from the cursor
        result = cursor.fetchall()

    return result

def select_column(column_name: str, table_name: str) -> str:
    query = f'select {column_name} from {table_name}'
    return query

f_name = 'Brad'
l_name = 'Pitt'
age = psycopg2.Date(1961,6,5)
num_oscars = 2

q = f"insert into actors (first_name, last_name, age, number_oscars) values ('{f_name}', '{l_name}', {age}, {num_oscars});"

def run_change_query(query: str): 
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()

run_change_query(q)
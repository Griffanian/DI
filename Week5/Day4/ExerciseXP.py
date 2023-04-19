import psycopg2
conn = psycopg2.connect(
host = 'localhost',
user = 'postgres',
password= '1234', 
dbname = 'postgres')

def setup_database():
    try:
        conn.autocommit = True
        sql = ''' CREATE database resturants '''
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.close()
    except:
        pass
    

def setup_table():
    conn = psycopg2.connect(
    host = 'localhost',
    user = 'postgres',
    password= '1234', 
    dbname = 'resturants')
    try:
        conn.autocommit = True
        sql = ''' CREATE table menu(
        name varchar(50),
        price int
        )'''
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.close()
    except:
        pass

def run_change_query(query: str):
    conn = psycopg2.connect(
    host = 'localhost',
    user = 'postgres',
    password= '1234', 
    dbname = 'resturants') 
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()

def run_select_query(query: str):
    conn = psycopg2.connect(
    host = 'localhost',
    user = 'postgres',
    password= '1234', 
    dbname = 'resturants')
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result

class MenuItem:
    instances={}
    def __init__(self,name:str,price:int) :
        self.name=name
        self.price=price
        MenuItem.instances.update({self.name:self})

    def save(self):
        if self.name not in [item[0] for item in MenuItem.all()]:
            run_change_query(f"insert into menu (name, price) values ('{self.name}','{self.price}')")

    def delete(self):
        run_change_query(f"delete from menu where name = '{self.name}'")

    def update(self,new_name,new_price):
        run_change_query(f"update menu set name = '{new_name}', price = '{new_price}' where name = '{self.name}'")

    def all():
        return run_select_query("select * from menu")

    def get_by_name(name):
        names_list=[item[0] for item in MenuItem.all()]
        if name in names_list:
            return MenuItem.instances[name]
print(MenuItem.all())
# item = MenuItem('Burger', 35)
# item.save()
# item.delete()
# item.update('Veggie Burger', 37)
# item2 = MenuItem.get_by_name('Beef Stew')
# items = MenuItem.all()
# print(item.name,item2,items)
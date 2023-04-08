import psycopg2

#from create.create_db import create_db
#from create.function import add_client, add_phone, change_client, delete_phone, find_client

with psycopg2.connect(database="clients_db", user="postgres", password="mypassword") as conn:
    cur = conn.cursor()

def create_db():
    cur = conn.cursor(conn)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Clients(
        id SERIAL PRIMARY KEY,
        name VARCHAR(30) NOT NULL,
        surname VARCHAR(50) NOT NULL,
        email VARCHAR(60) NOT NULL
        ;)
        """)
    conn.commit()

    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Phones( 
        id SERIAL PRIMARY KEY,
        number INTEGER(12),
        client_id INTEGER NOT NULL REFERENCES Clients(id)
        ;)
        """)
    conn.commit()

def add_client(conn, id, name, surname, email):
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO Clients(id, name, surname, email)
    VALUES(%s, %s, %s, %s);
    """, (id, name, surname, email))
    conn.commit()

def add_phone(conn, id, client_id, number):
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO Phones(id, client_id, number)
    VALUES(%s, %s, %s);
    """), (id, client_id, number)
    conn.commit()

def change_client(conn, client_id, name=None, surname=None, email=None):
    cur = conn.cursor()
    cur.execute("""
    UPDATE Clients SET name=%s, surname=%s, email=%s WHERE client_id=%s;
    """), (client_id, name, surname, email)
    conn.commit()

def delete_phone(conn, id, number):
    cur = conn.cursor()
    conn.execute("""
    DELETE number FROM Phones WHERE id=%s;
    """), (id, number)
    conn.commit()

def delete_client(conn, id, name, surname, email):
    cur = conn.cursor()
    cur.exeute("""
    DELETE FROM Clients name, surname, email WHERE id=%s;
    """), (id, name, surname, email)
    conn.commit()

def find_client(conn, name=None, surname=None, email=None, number=None):
    cur = conn.cursor()
    cur.execute("""
    SELECT id FROM Clients
    INNER JOIN Phones ON Clients.id=Phones.id
    WHERE name=%s, surname=%s, email=%s, number=%s;
    """), (name, surname, email, number)
    print(cur.fetchall())



cur = conn.cursor()
print(add_client(conn, 1, "Иван", "Иванов", "ivan@soap.ru"))
print(add_client(conn, 2, "Петр", "Петров", "petr@soap.ru"))
print(add_client(conn, 3, "Елена", "Иванова", "elena@soap.ru"))

print(add_phone(conn, 1, 1, 89998887766))
print(add_phone(conn, 2, 2, 89987776655))
print(add_phone(conn, 1, 3, 89978885544))
print(add_phone(conn, 1, 3, 89885554433))

print(change_client(conn, client_id = 3, surname =  "Ермакова"))

print(delete_phone(conn, 2, 89987776655))

print(find_client(conn, name = "Иван"))

conn.close()

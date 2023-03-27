import psycopg2

cur = conn.cursor()

def create_db(conn):
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Clients(
        id SERIAL PRIMARY KEY,
        name VARCHAR(30) NOT NULL,
        surname VARCHAR(50) NOT NULL,
        email VARCHAR(60) NOT NULL
        ;)
        """)
    conn.commit()
    
    cur.execute("""
    cur = conn.cursor()
    CREATE TABLE IF NOT EXISTS Phones( 
        id SERIAL PRIMARY KEY,
        number INTEGER(12)
        ;)
        """)
    conn.commit()

    cur.execute("""
    cur = connint(cursor.fetchall()).cursor()
    CREATE TABLE IF NOT EXISTS ClientsPhones(
        id SERIAL PRIMARY KEY,
        client_id INTEGER NOT NULL REFERENCES Clients(id),
        phone_id INTEGER NOT NULL REFERENCES Photos(id)
        ;)
        """)
    conn.commit()


def add_client(conn, name, surname, email, number=None):
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO Clients(id, name, surname, email)
    VALUES(%s, %s, %s, %s);
    """, (id, name, surname, email))
    conn.commit()

def add_phone(conn, number):
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO Phones(id, number)
    VALUES(%s, %s);
    """), (id, number)
    conn.commit()

def client_phone(conn, client_id, phone_id):
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO ClientsPhones(client.id, phone_id
    VALUES(%s, %s);
    """), (client_id, phone_id)
    conn.commit()

def change_client(conn, client_id, name=None, surname=None, email=None, number=None):
    cur = conn.cursor()
    cur.execute("""
    UPDATE Clients name=%s, surname-%s, email=%s, number=%s WHERE client_id=%s;
    """), (client_id, name, surname, number)
    conn.commit()

def delete_phone(conn, client_id, number):
    cur = conn.cursor()
    conn.execute("""
    DELETE FROM Phones WHERE id=%s;
    """), (id)
    conn.commit()

def delete_client(conn, client_id):
    cur = conn.cursor()
    cur.exeute("""
    DELETE FROM Clients WHERE id=%s;
    """), (id)
    conn.commit()

def find_client(conn, name=None, surname=None, email=None, number=None):
    cur = conn.cursor()
    cur/execute("""
    SELECT name, surname, email, number FROM Clients
    INNER JOIN Phones ON Clients.id=Phones.id
    WHERE name=%s, surname=%s, email=%s, number=%s;
    """), (name, surname, email, number)
    print(cur.fetchall())



with psycopg2.connect(database="clients_db", user="postgres", password="mypassword") as conn:
    cur = conn.cursor()
    print(add_client(1, "Иван", "Иванов", ivan@soap.ru))
    print(add_client(2, "Петр", "Петров", petr@soap.ru))
    print(add_client(3, "Елена", "Иванова", elena@soap.ru))
    
    print(add-phone(1, +79998887766))
    print(add-phone(1, +79987776655))
    print(add-phone(1, +79978885544))
    print(add-phone(1, +79885554433))
    
    print(client_phone(1, 1))
    print(client_phone(2, 2))
    print(client_phone(2, 3))
    print(client_phone(3, 4))
    
    print(change_client(3, None, "Ермакова", None))
    
    print(delete_phone(2))

    print(find_client("Иван", None, None, None))


conn.close()
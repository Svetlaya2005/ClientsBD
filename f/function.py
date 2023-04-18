from main import conn
with conn.cursor() as cur:
    def create_db():
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Clients(
            id SERIAL PRIMARY KEY,
            name VARCHAR(30) NOT NULL,
            surname VARCHAR(50) NOT NULL,
            email VARCHAR(60) NOT NULL
            ;)
            """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS Phones( 
            id SERIAL PRIMARY KEY,
            number INTEGER(12),
            client_id INTEGER NOT NULL REFERENCES Clients(id)
            ;)
            """)
def add_client(conn, id, name, surname, email):
    cur.execute("""
    INSERT INTO Clients(id, name, surname, email)
    VALUES(%s, %s, %s, %s);
    """, (id, name, surname, email))

def add_phone(conn, id, client_id, number):
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO Phones(id, client_id, number)
    VALUES(%s, %s, %s);
    """), (id, client_id, number)

def change_client(conn, client_id, name=None, surname=None, email=None, number=None):
    cur = conn.cursor()
    cur.execute("""
    IF name is not None THEN
        UPDATE Clients SET name=%s WHERE client_id=%s;
    END IF;
    IF surname is not None THEN
        UPDATE Clients SET surname=%s WHERE client_id=%s;
    END IF;
    IF email is not None THEN
        UPDATE Clients SET email=%s WHERE client_id=%s;
    END IF;    
    IF number is not None THEN
        UPDATE Phones SET number=%s WHERE client_id=%s;
    END IF;
    """), (conn, client_id, name, surname, email, number)

def delete_phone(conn, id, number):
    cur = conn.cursor()
    conn.execute("""
    DELETE number FROM Phones WHERE id=%s;
    """), (id, number)

def delete_client(conn, id, name, surname, email):
    cur = conn.cursor()
    cur.exeute("""
    DELETE FROM Clients name, surname, email WHERE id=%s;
    """), (id, name, surname, email)

def find_client(conn, name=None, surname=None, email=None, number=None):
    cur = conn.cursor()
    cur.execute("""
    IF name is not None THEN
        SELECT id FROM Clients WHERE name=%s;
    END IF;
    IF surname is not None THEN
        SELECT id FROM Clients WHERE surname=%s;
    END IF;
    IF email is not None THEN
        SELECT id FROM Clients WHERE email=%s;
    END IF;
    IF number is not None THEN
        SELECT id FROM Phones WHERE number=%s;
    END IF;
    """), (name, surname, email, number)

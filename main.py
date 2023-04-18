import psycopg2
from f.function import create_db, add_client, add_phone, change_client, delete_phone, find_client

with psycopg2.connect(database="clients_db", user="postgres", password="mypassword") as conn:
    with conn.cursor() as cur:
def main():
    print(create_db(conn))

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

if __name__=="__main__":
    main()
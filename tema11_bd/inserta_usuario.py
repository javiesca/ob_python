import sqlite3



def main():
    id = input("ID de usuario: ")
    username = input("Inserta nombre de usuario: ")
    password = input("Introduce contraseña: ")
    inserta_usuario(id, username, password)

def inserta_usuario(id, usuario, password):
    conn = sqlite3.connect('miaplicacion.db', isolation_level=None)
    cursor = conn.cursor()

    query = f"INSERT INTO users (id, username, password) VALUES ({id}, '{usuario}', '{password}')"
    rows = cursor.execute(query)
    print(type(rows))

    conn.commit()

    cursor.close()
    conn.close()


if __name__=='__main__':
    main()
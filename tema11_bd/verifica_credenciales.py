import getpass
import sqlite3


def main():
    username = input("Nombre de usuario: ")
    password = getpass.getpass("Comtraseña: ")

    if verifica_credenciales(username, password):
        print("Login correcto")
    else:
        print("Login incorrecto")

def verifica_credenciales(username, password):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()

    query = f"SELECT id FROM users WHERE username = '{username}' AND password = '{password}'"
    print("Query a ejecutar ", query)

    rows = cursor.execute(query)
    data = rows.fetchone()
    print("Data es ", type(data))

    cursor.close()
    conn.close()

    if data == None:
        return False

    return True

if __name__ == '__main__':
    main()


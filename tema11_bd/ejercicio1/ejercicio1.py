import sqlite3


def main():
    menu()

def menu():
    print("-------NENU--------")
    print("")
    print("1. INSERTAR ALUMNOS")
    print("2. CONSULTAR ALUMNO POR NOMBRE")
    print("3. SALIR")
    opcion = int(input("Introduzca una opción..."))
    while opcion !=3:
        if opcion == 1:
            inserta_alumno()
        elif opcion == 2:
            busca_alumno()
        elif opcion == 3:
            print("SALIENDO DEL PROGRAMA")


def inserta_alumno():
    numero_alumnos = int(input("Cuantos Alumnos deseas insertar?"))
    contador = 0
    conn = sqlite3.connect('miBasedeDatos.db', isolation_level=None)

    while contador < numero_alumnos:
        id = input("ID del usuario: ")
        nombre = input("Inserta el nombre del Alumno: ")
        apellido = input("Inserta el apellido del Alumno: ")
        cursor = conn.cursor()
        query = f"INSERT INTO Alumnos (id, nombre, apellido) VALUES({id}, '{nombre}', '{apellido}')"
        cursor.execute(query)
        conn.commit()
        cursor.close()
        contador = contador + 1


    conn.close()
    print(f"Se han insertado {contador} alumnos en la base de datos.")
    main()


def busca_alumno():
    nombreBuscar = input("Nombre a buscar: ")

    conn = sqlite3.connect('miBasedeDatos.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM Alumnos WHERE nombre = '{nombreBuscar}'"

    cursor.execute(query)
    print(cursor.fetchone())

    cursor.close()
    conn.close()
    main()



if __name__ == '__main__':
    main()

def main():
    usuarios = listarUsuarios()
    cont = 1
    for usuario in usuarios:
        print(f'Usuario {cont}: {usuario}')
        cont+=1

def listarUsuarios():
    f = open('/etc/passwd', 'r')
    datos = f.readlines()
    f.close()

    resultado = []
    for linea in datos:
        if linea[0] == '#' or linea[0] == '_':
            continue

        partes = linea.split((':'))
        resultado.append(partes[0])

    return resultado

if __name__ == '__main__':
    main()
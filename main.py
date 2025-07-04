#Funcion crear nuevo usuario
def registrar_usuario(usuarios):
    usuario = input("Nombre de usuario: ").strip()
    if usuario in usuarios:
        print("El usuario ya existe. Intente con otro nombre.")
        return
    password = input("Contraseña ")
    usuarios[usuario] = password
    print("Usuario registrado con exito.")
#Utilizo un diccionario(usuarios) para almacenar los usuarios(clave) y sus contraseñas(valor)


# Login para usuarios registrados. Comprueba la contraseña.
def login_usuario(usuarios):
    usuario = input("Usuario: ").strip()
    password = input("Contraseña: ")
    if usuarios.get(usuario) == password:
        print("Login exitoso!")
    else:
        print("Credenciales incorrectas")

# Listado de usuarios Registrados
def mostrar_usuarios(usuarios):
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    print("Usuarios registrados:")
    for nombre in usuarios:
        print("{nombre}")
    print()

#Menu Principal
def menu():
    usuarios = {}
    while True:
        print("1. Registrar usuario")
        print("2. Login")
        print("3. Mostrar usuarios")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            registrar_usuario(usuarios)
        elif opcion == "2":
            login_usuario(usuarios)
        elif opcion == "3":
            mostrar_usuarios(usuarios)
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")
        print()
#Usé elseif, podrias decirme si hay alguna otra opcion mas clara de hacerlo?

#Llamo al menu
menu()

    
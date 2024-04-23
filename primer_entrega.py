# Función para registrar un nuevo usuario
def registrar_usuario(database):
    nombre_de_usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese contraseña: ")
    
    
    database[nombre_de_usuario] = {"Contraseña": contraseña}
    print("Usuario registrado exitosamente.")

# Función para listar usuarios
def listar_usuarios(database):
    print("Base de datos de usuarios:")
    print(database)

# Función principal
def main():
    base_de_datos = {}
    interactuando = True

    while interactuando:
        opcion = input("Seleccione una opción (registrar usuario/listar usuarios/salir): ")
        
        if opcion.lower() == "registrar usuario":
            registrar_usuario(base_de_datos)
        elif opcion.lower() == "listar usuarios":
            listar_usuarios(base_de_datos)
        elif opcion.lower() == "salir":
            interactuando = False
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
import getpass

# Simulación de usuarios
usuarios = [
    {"usuario": "Dolo", "nombre": "Dolores_Fernandez", "contrasena": "1234", "rol": "estandar"},
    {"usuario": "Fran", "nombre": "Franco_Fernandez", "contrasena": "1234", "rol": "estandar"},
    {"usuario": "Lore", "nombre": "Lorena_Figueroa", "contrasena": "1234", "rol": "estandar"},
    {"usuario": "Mati", "nombre": "Matias_Rodriguez", "contrasena": "1234", "rol": "admin"},
    {"usuario": "Ale", "nombre": "Ale_Gariglio", "contrasena": "1234", "rol": "admin"}
]
# Ver datos personales 
def mostrar_datos_personales(usuario):
    print(f"\n Tus datos:")
    print(f"Nombre: {usuario['nombre']}")
    print(f"Usuario: {usuario['usuario']}")
    print(f"Rol: {usuario['rol']}\n")
# Ver lista de todos los usuarios
def mostrar_usuarios():
    print("\n Lista de usuarios registrados:")
    for u in usuarios:
        print(f"- {u['usuario']} ({u['rol']})")
#cambiar rol
def cambiar_rol():
    target = input("Ingrese el nombre de usuario a cambiar rol: ")
    for u in usuarios:
        if u["usuario"] == target:
            nuevo_rol = input("Nuevo rol (admin/estandar): ")
            if nuevo_rol in ["admin", "estandar"]:
                u["rol"] = nuevo_rol
                print("Rol actualizado.")
            else:
                print("X Rol no válido.")
            return
    print("X Usuario no encontrado.")
# Eliminar usuario
def eliminar_usuario():
    target = input("Ingrese el nombre de usuario a eliminar: ")
    for u in usuarios:
        if u["usuario"] == target:
            usuarios.remove(u)
            print("Usuario eliminado.")
            return
    print("X Usuario no encontrado.")

# Login
usuario_autenticado = None

print("Seleccione el tipo de Usuario: ")
print("1. Administrador")
print("2. Usuario Estándar")

tipo_usuario = None
while tipo_usuario is None:
    opcion = input("Ingrese el número de opción: ")
    if opcion == "1":
        tipo_usuario = "admin"
    elif opcion == "2":
        tipo_usuario = "estandar"
    else:
        print("Opción inválida. Intente nuevamente.")

# Autenticación
while usuario_autenticado is None:
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    contrasena = getpass.getpass("Ingrese la contraseña: ")

    for u in usuarios:
        if u["usuario"] == nombre_usuario and u["contrasena"] == contrasena and u["rol"] == tipo_usuario:
            usuario_autenticado = u
            print(f"\n Bienvenido {u['nombre']} ({u['rol']})")
            break
    if usuario_autenticado is None:
        print("X Usuario o contraseña incorrectos. Intente nuevamente.\n")

# Menú según rol
while True:
    print("\n--- MENÚ ---")

    if usuario_autenticado["rol"] == "admin":
        print("1. Ver lista de usuarios")
        print("2. Cambiar rol de un usuario")
        print("3. Eliminar un usuario")
        print("4. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_usuarios()
        elif opcion == "2":
            cambiar_rol()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            print("Sesión cerrada.")
            break
        else:
            print("Opción inválida.")

    elif usuario_autenticado["rol"] == "estandar":
        print("1. Ver mis datos personales")
        print("2. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_datos_personales(usuario_autenticado)
        elif opcion == "2":
            print("Sesión cerrada.")
            break
        else:
            print("Opción inválida.")

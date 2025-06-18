import getpass
import variables

# Ver datos personales 
def mostrar_datos_personales(usuario):
    print(f"\n Tus datos:")
    print(f"Nombre: {usuario['nombre']}")
    print(f"Usuario: {usuario['usuario']}")
    print(f"Rol: {usuario['rol']}\n")
# Ver lista de todos los usuarios
def mostrar_usuarios():
    print("\n Lista de usuarios registrados:")
    for u in variables.usuarios:
        print(f" {u['usuario']} - {u['nombre']} ({u['rol']})")
#cambiar rol
def cambiar_rol():
    target = input("Ingrese el nombre de usuario a cambiar rol: ")
    for u in variables.usuarios:
        if u["usuario"] == target:
            nuevo_rol = input("Nuevo rol (Administrados/Usuario): ")
            if nuevo_rol in ["Administrador", "Usuario"]:
                u["rol"] = nuevo_rol
                print("Rol actualizado.")
            else:
                print("X Rol no válido.")
            return
    print("X Usuario no encontrado.")
# Eliminar usuario
def eliminar_usuario():
    target = input("Ingrese el nombre de usuario a eliminar: ")
    for u in variables.usuarios:
        if u["usuario"] == target:
            variables.usuarios.remove(u)
            print("Usuario eliminado.")
            return
    print("X Usuario no encontrado.")
# Agregar usuario
def agregar_usuario():
    nombre = input("Nombre: ")
    usuario = input("Usuario: ")
    contrasena = getpass.getpass("Contraseña: ")
    rol = input("Rol (Administrador/Usuario): ")
    if rol in ["Administrador", "Usuario"]:
        variables.usuarios.append({"nombre": nombre, "usuario": usuario, "contrasena": contrasena, "rol": rol})
        print("Usuario agregado.")
    else:
        print("X Rol no válido.")

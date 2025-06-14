import os
import subprocess
import getpass
import variables
import menu

def main():
    # Login
    usuario_autenticado = None
    # Autenticación
    while usuario_autenticado is None:
        print("Seleccione el tipo de Usuario: ")
        print("1. Administrador")
        print("2. Usuario Estándar")

        UserType = (input("Ingrese el número de opción: "))
        if UserType == "1":
            print("Administrador")
            tipo_usuario="Administrador"
        elif UserType == "2":
            print("Usuario")
            tipo_usuario="Usuario"
        else:
            print("Error: Opción no válida. Intente nuevamente")
            print("")
        nombre_usuario = input("Ingrese el Nombre de Usuario: ")
        contrasena = getpass.getpass("Ingrese la Contraseña:")
        for u in variables.usuarios:
            if u["usuario"] == nombre_usuario and u["contrasena"] == contrasena and u["rol"] == tipo_usuario:
                usuario_autenticado = u
                print(f"\n Bienvenido {u['nombre']} ({u['rol']})")
                subprocess.run(menu.main(usuario_autenticado))
                break
        if usuario_autenticado is None:
            print("X Usuario o contraseña incorrectos. Intente nuevamente.\n")

if __name__ == "__main__":
    main()
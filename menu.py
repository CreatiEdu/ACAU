import getpass

import crud

def main(usuario_autenticado):
    flag = True
    # Menú según rol
    while flag:
        print("\n--- MENÚ ---")

        if usuario_autenticado["rol"] == "Administrador":
            print("1. Ver lista de Usuarios")
            print("2. Cambiar rol de un Usuario")
            print("3. Agregar un Usuario")
            print("4. Eliminar un Usuario")
            print("5. Cerrar sesión")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                crud.mostrar_usuarios()
            elif opcion == "2":
                crud.cambiar_rol()
            elif opcion == "3":
                crud.agregar_usuario()
            elif opcion == "4":
                crud.eliminar_usuario()
            elif opcion == "5":
                print("Sesión cerrada.")
                flag = False
                pass
            else:
                print("Opción inválida.")

        elif usuario_autenticado["rol"] == "Usuario":
            print("1. Ver mis datos personales")
            print("2. Cerrar sesión")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                crud.mostrar_datos_personales(usuario_autenticado)
            elif opcion == "2":
                print("Sesión cerrada.")
                flag = False
                pass
            else:
                print("Opción inválida.")

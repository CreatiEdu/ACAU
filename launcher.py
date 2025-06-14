from menu import agregar_usuario
import subprocess
import login

def main():
     while True:
        print('¡Bienvenido! Seleciona una opción para avanzar:')
        print('1. Registar un usuario')
        print('2. Iniciar sesión')
        print('3. Salir del programa')
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            agregar_usuario()
        elif opcion == '2':
            login.main()
        elif opcion == '3':
            print("Sesión terminada.")
            break
        else:
            print("Opción inválida, Intente nuevamente.")

if __name__ == "__main__":
    main()
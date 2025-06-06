import getpass

# Variables base
DemoUser = "User"
DemoPass = "1234"
IsOk = True
IsUser = False
#
while IsUser == False:
# Ingesar el tipo de Usuario
    print("Seleccione el tipo de Usuario: ")
    print("1. Administrador")
    print("2. Usuario")
    UserType = int(input("Ingrese el número de opción: "))
    if UserType == 1:
        print("Administrador")
        IsOk=False
    elif UserType == 2:
        print("Usuario")
        IsOk=False
    else:
        print("Error: Opción no válida. Intente nuevamente")
        print("")
    
    while IsOk == False:
    # Ingresar el Usuario
        User = input("Ingrese el Nombre de Usuario: ")
        # Ingresar la Contraseña
        Password = getpass.getpass("Ingrese la Contraseña:")
        if User == DemoUser and Password == DemoPass and (UserType == 1 or UserType == 2):
            print("Bienvenido")
            IsUser=True
        else:
            print("Error: El Usuario o la Contraseña son incorrectos. Intente nuevamente")
        
        IsOk = True
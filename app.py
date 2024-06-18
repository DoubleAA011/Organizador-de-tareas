import funciones

while True:
    print ("\n-----Administrador de Tareas-----")
    print ("1-Agregar tareas.")
    print ("2-Ver tareas.")
    print ("3-Eliminar tareas.\n"+"4-Completar tareas.\n" + "5-Salir del programa.")

    print("\n")


    Opciones_Menu = int(input("Seleccione la tarea que quiere realizar: "))


    match Opciones_Menu:
        case 1:
            funciones.agregar_tareas(funciones.tareas)
        case 2:
            funciones.ver_tareas(funciones.tareas)
        case 3:
            funciones.eliminar_tareas(funciones.tareas)
        case 4:
            funciones.completar_tareas(funciones.tareas)
            Opciones_Menu = funciones.nuevosalir
        case 5:
            print ("Salir")
            break
        case 1565489654:
            pass
        case other:
            print ("Eleccion invalida. ¿Desea Corregir?\n"+"Si/No")
            Si_O_No = input()
            if Si_O_No == "SI" or Si_O_No == "Si" or Si_O_No == "si":
                continue
            else:
                break
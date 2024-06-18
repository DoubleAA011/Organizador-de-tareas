tareas = []
nuevosalir = 1565489654



def agregar_tareas(tareas):
    
    Nueva_Tarea = input("Ingrese la nueva tarea: ")

    tareas.append(Nueva_Tarea)

    Verificar_tareas = tareas.count(Nueva_Tarea)

    if Verificar_tareas>1:
        Si_O_No = input("La tarea ya fue agregada con anterioridad. ¿Desea eliminarla? (si/no): ")


        if Si_O_No == "si" or Si_O_No == "SI" or Si_O_No == "Si":
            eliminar_tareas(tareas)


    else:
        print(f"La tarea `{Nueva_Tarea}` fue agregada con éxito.")

        print (Nueva_Tarea)

        Numero_Tarea = tareas.index(Nueva_Tarea)

        print (Numero_Tarea + 1)

        return tareas
    





def ver_tareas(tareas):
    if len(tareas) > 0 :
        print(f"Sus tareas pendientes son: {tareas}")
    else:
        Si_O_No = input("Aun no tiene tareas para completar. ¿Desea agregar tareas? si/no: ")
        if Si_O_No == "si" or Si_O_No == "SI" or Si_O_No == "Si":
            agregar_tareas(tareas)






def eliminar_tareas(tareas):
    tareas_eliminar = input("¿Que tarea desea eliminar?: ")
    Num_De_Esas_Tareas = tareas.count(tareas_eliminar)
    if Num_De_Esas_Tareas >= 1:
        tareas.remove(tareas_eliminar)
        print("Tarea removida con exito")
        return tareas
    else:
        Si_O_No = input("Su tarea no existe en el listado de tareas pendientes. ¿Desea agregarla? Si/No:")
        if Si_O_No == "si" or Si_O_No == "SI" or Si_O_No == "Si":
            agregar_tareas(tareas)
        else:
            eliminar_tareas(tareas)






def completar_tareas(tareas):
    ver_tareas(tareas)
    Tareas_Completadas = []
    Nueva_Completada = input("Ingrese la tarea que quiere completar: ")
    if tareas.count(Nueva_Completada) >0:
        if Tareas_Completadas.count(Nueva_Completada)>0 and tareas.count(Nueva_Completada)<1:
            print ("Usted ya completo dicha tarea.")
            Si_O_No = input ("¿Desea completar otra tarea? Si/No: ")
            if Si_O_No == "si" or Si_O_No == "SI" or Si_O_No == "Si":
                agregar_tareas(tareas)
            else: 
                nuevosalir = 5
                return nuevosalir 
        else:
            Tareas_Completadas.append(Nueva_Completada)
            tareas.remove(Nueva_Completada)
            return tareas
    else:
        Si_O_No = input("Su tarea no existe en el listado de tareas pendientes. ¿Desea agregarla? Si/No:")
        if Si_O_No == "si" or Si_O_No == "SI" or Si_O_No == "Si":
            agregar_tareas(tareas)



    



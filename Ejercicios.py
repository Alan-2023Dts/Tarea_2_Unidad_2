def ejercicio_1():
    #Aqui va el ejercicio_1
    Num_1 = int(input("Ingrese el primer número: "))
    Num_2 = int(input("Ingrese el segundo número: "))
    if Num_1 > Num_2: # compara el numero 1 con el numero 2
        print(f"El número mayor es: {Num_1}")
    elif Num_2 > Num_1: #compara el numero 2 con el numero 1
        print(f"El número mayor es: {Num_2}")
    pass
  
                                                                                                                                 
def ejercicio_2():
    #Aqui va el ejercicio_2
    pass
def ejercicio_3():
   #Aqui va el ejercicio_3
    pass
    
def ejercicio_4():
    #Aqui va el ejercicio_4
    pass

def ejercicio_5():
    #Aqui va el ejercicio_5
    pass

def ejercicio_6():
    #Aqui va el ejercicio_6
    pass 

def ejercicio_7():
    #ejercicio 7
    pass

def ejercicio_8():
    #ejercicio 8
    pass

def ejercicio_9():
    #Aqui va el ejercicio_9 
    pass

def ejercicio_10():
    #Aqui va el ejercicio_10
    pass

def ejercicio_11():
    #Aqui va el ejercicio_11
    pass

def ejercicio_12():
    #Aqui va el ejercicio_12
    pass

def ejercicio_13():
    #Aqui va el ejercicio_13
   pass

def ejercicio_14():
    #Aqui va el ejercicio_14
    pass

def ejercicio_15():
    #Aqui va el ejercicio_15
   pass

def ejercicio_16():
    #Aqui va el ejercicio_16
    pass

###################################################################################################################
  
# Diccionario tipo switch
switch = {
    1: ejercicio_1,
    2: ejercicio_2,
    3: ejercicio_3,
    4: ejercicio_4,
    5: ejercicio_5,
    6: ejercicio_6,
    7: ejercicio_7,
    8: ejercicio_8,
    9: ejercicio_9,
    10: ejercicio_10,
    11: ejercicio_11,
    12: ejercicio_12,
    13: ejercicio_13,
    14: ejercicio_14,
    15: ejercicio_15,
    16: ejercicio_16
}
###################################################################################################################
# Función principal
def main():
    while True:
        print("--- Menú de ejercicios ---")
        for i in range(1,17): # un for que va del 1 al 16
            print(f"{i}. Ejercicio {i}") # Mostrar opciones del 1 al 16 la f es para que reconozca la i como variable
        print("0. Salir")# despues de terminar el for imprimimos la opcion para cerrar el programa
        
        opcion = int(input("Seleccione una opción (0-16): ")) # Solicita al usuario que ingrese una opción
        if opcion == 0:# si la opcion es 0 se cierra el programa
            print("Saliendo del programa...")
            break # break para salir del bucle
        elif opcion in switch: # si la opcion esta en el diccionario switch
            switch[opcion]() # llama a la funcion correspondiente
        else:
            print("Opción no válida. Intente de nuevo.") # si la opcion no es valida imprime este mensaje
# 🔹 Ejecutar main
if __name__ == "__main__": #sirve para que se ejecute el main  (la función principal) Propuesta por copilot
    main() #Llama a la función principal para iniciar el programa postdata : Es lo malo de acostumbrarse a c# :(

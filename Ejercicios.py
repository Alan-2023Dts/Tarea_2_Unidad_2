import math
def ejercicio_1():
    #Aqui va el ejercicio_1
    Num_1 = int(input("Ingrese el primer número: "))
    Num_2 = int(input("Ingrese el segundo número: "))
    if Num_1 > Num_2: # compara el numero 1 con el numero 2
        print(f"El número mayor es: {Num_1}")
    elif Num_2 > Num_1: #compara el numero 2 con el numero 1
        print(f"El número mayor es: {Num_2}")
    pass

    #Aqui va el ejercicio_7
    pass                                                                                                                       
                                                                                                                    
def ejercicio_2():
    #Aqui va el ejercicio_2
    print ("sistema de comparacion de numeros")
    a=int(input("ingrese el primer numero"))
    b=int(input("ingrese el segundo numero"))
    c=int(input("ingrese el tercer numero"))
    #filtrado para evitar que las cantidades no sean iguales
    if a==b or b==c or c==a:
        print("las cantidades no pueden ser iguales")
    else:
        #comparacion de las cantidades para obtener la cantidad mayor
        if a>b and a>c:
            r1="la cantidad mas grande es ", a
        elif b>a and b>c:
            r1="la cantidad mas grande es ", b
        else:
            r1="la cantidad mas grande es ", c
        #comparación de las cantidades para optner la cantidad menor
        if a<b and a<c:
            r2="la cantidad mas pequeña es ", a
        elif b<a and b<c:
            r2="la cantidad mas pequeña es ", b
        else:
            r2="la cantidad mas pequeña es ", c
        print (r1)
        print (r2)
    pass
def ejercicio_3():
    #Aqui va el ejercicio_3
    print("Suma hasta el numero 10 ")
    total = 0
    for i in range(1, 11):  # Contador para llegar hasta 10
        total += i
    print(f"La suma es: {total}")

     
 
    
def ejercicio_4():
    #Aqui va el ejercicio_4
    import math
    m=input("¿el triangulo tiene un angulo de 90 grados? si/no")
    if m=="si":
        print ("sistema para obtener hipotenusa de un triangulo rectangulo")
        print ("1----por teorema de pitagoras")
        print ("2----por trigonometria")
        print ("3----salir")
        a=int(input("seleccione una opción"))
        match a:
            case 1:
                b=int(input("ingrese el cateto opuesto"))
                c=int(input("ingrese el cateto adyacente"))
                d=math.sqrt((b**2)+(c**2))
                print("la hipotenusa del triangulo es igual a ", d)
                e=int(input("si desea continuar con la comproacion presione 1 de locontrario presione 2"))
                match e:
                    case 1:
                        f=(b**2)+(c**2)
                        if d==f:
                            print ("el resultado es correcto")
                    case 2:
                        print ("hasta luego")
            case 2:
                print("que cateto conoce")
                print("1------adyacente")
                print("2------opuesto")
                b=int(input("seleccione una opción"))
                match b:
                    case 1:
                        c=int(input("ingrese la medida del angulo"))
                        d=int(input("ingrese la medida del angulo adyacente"))
                        e=d/math.cos(c)
                        print("la hipotenusa del triangulo es igual a",e )
                    case 2:
                        c=int(input("ingrese la medida del angulo"))
                        d=int(input("ingrese la medida del angulo opuesto"))
                        e=d/math.sin(c)
                        print("la hipotenusa del triangulo es igual a",e )
            case 3:
                print ("hasta luego")

    pass

def ejercicio_5():
    #Aqui va el ejercicio_5
    Radio = float(input("Ingrese el radio del cilidro: "))
    Altura = float(input("Ingrese la Altura del cilindro: "))
    
    Area = 2 * math.pi * Radio * (Radio + Altura)
    Volumen = math.pi * math.pow(Radio,2) * Altura
    
    print(f"El Area del cilindro es de: {Area}")
    print(f"El Volumen del cilindro es de: {Volumen}" )
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

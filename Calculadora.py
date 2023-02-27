# El siguiente código esta diseñado para calcular vectores en r3 
# Al ejecutar el código nos encontraremos con un menú en el cual podrá seleccionar el o los cálculos que desee realizar
# Mencionar además que para la correcta ejecución debemos instalar la bibliotecas numpy

import os                                                              #Comenzamos importando las bliblioteca os
import numpy as np                                                     #junto con la biblioteca numpy

def Suma_de_vectores(a,b):                                             #Comenzamos programando la funcion encargada de 
    vector_final = [a[0]+b[0],a[1]+b[1],a[2]+b[2]]                     #sumar 2 vectores. Para esto trabajaremos con las posiciones
    return vector_final                                                #del ambos vectores, en donde a representa el vector x y b el vector y.

def Producto_punto(a,b):                                               #Avanzamos a la función que nos permitirá calcular
    vector1 = np.array([a[0],a[1],a[2]])                               #el producto punto entre dos vectores, para esto igualmente 
    vector2 = np.array([b[0],b[1],b[2]])                               #trabajamos con las posiciones de los 2 vectores para realizar de manera óptima el 
    vector_final = vector1.dot(vector2)                                #calculo. Además mencionar que el constructor "np" es propia de numpy. 
    return vector_final

def Producto_cruz(a,b):                                                #Avanzamos en el código y ahora definimos una función que calcule
    vector1 = np.array([a[0],a[1],a[2]])                               #el producto cruz entre dos vectores, esto con la misma lógica
    vector2 = np.array([b[0],b[1],b[2]])                               #de las funciones anteriores.
    vector_final = np.cross(vector1,vector2)
    return vector_final

def Suma_de_vectores(a,b):                                             #Posteriormente definimos la función encargada de 
    vector_final = [a[0]+b[0],a[1]+b[1],a[2]+b[2]]                     #sumar dos vectores, esta al igual que todas las demás funciones
    return vector_final                                                #fueron trabajadas con las posiciones de tanto del vector X como el Y.

def Producto_escalar(a,c):                                             #Continuamos con la última función de operaciones 
    vector_final = [c*a[0],c*a[1],c*a[2]]                              #la cual nos permitirá calcular el producto escalar entre un vector
    return vector_final                                                #y un escalar designado por el usuario.

def menu():                                                            #En este punto realizamos un pequeño menú de opciones para hacer esta calculadora
    try:                                                               #un poco más dinámica y entretenida, en donde el usuario ingresará de manera
        print('Ingrese valores del primer vecto: ')                    #arbitraria los valores de cada vector o escalar.
        v1 = float(input('1:'))
        v2 = float(input('2:'))
        v3 = float(input('3:'))
        print('Ingrese valores del segundo vecto: ')
        v4 = float(input('1:'))
        v5 = float(input('2:'))
        v6 = float(input('3:'))
        vector1 = [v1,v2,v3]
        vector2 = [v4,v5,v6]
        return vector1, vector2  

    except:
        os.system('clear')
        print('OPCIÓN INVALIDA')
        exit()

def menu2():                                                           #Menu para el caso de la función escalar
    try:
        print('Ingrese valores del vecto: ')
        v1 = float(input('1:'))
        v2 = float(input('2:'))
        v3 = float(input('3:'))
        print('Ingrese valor de escalar: ')
        e = float(input('Escalar: '))

        vector1 = [v1,v2,v3]
        os.system('clear')

        print('El resultado es: ',Producto_escalar(vector1,e))

    except:
        os.system
        print('OPCIÓN INVALIDA')
        exit()

if __name__ == "__main__":                                                    #De este main hacemos el llamado a cada función según la opcion que ingrese
#                                                                              el usuario, manteniendo siempre el control de los errores que podrían  
    while True:                                                               #verse reflejados.
        print('--------CALCULADORA DE VECTORES----------')
        print('Que operación desea realizar: ')
        print('1) Cálculo de SUMA DE VECTORES')   
        print('2) Cálculo de producto PUNTO')
        print('3) Cálculo de producto ESCALAR')
        print('4) Cálculo de producto CRUZ')
        print('0) Salir')

        r = int(input('Ingrese una opción: '))
        while r != 1 and r != 2 and r != 3 and r != 4 and r != 0:
            r = int(input('Ingrese opción válida: '))

        if r == 1:
            os.system('clear')
            vector1,vector2 = menu()
            os.system('clear')
            print('El resultado es: ',Suma_de_vectores(vector1,vector2))
            input('Presione una tecla para continuar...')

        if r == 2:
            os.system('clear')
            vector1,vector2 = menu()
            os.system('clear')

            print('El resultado es: ', Producto_punto(vector1, vector2))
            input('Presione una tecla para continuar...')

        if r == 3:
            os.system('clear')
            menu2()
            input('Presione una tecla para continuar...') 
            
        if r == 4:
            os.system('clear')
            vector1,vector2 = menu()
            os.system('clear')
            
            print('El resultado es: ', Producto_cruz(vector1, vector2))
            input('Presione una tecla para continuar...')

        if r == 0:
            exit()

"""
Juego de Python
Integrantes:
- Alan Jumbo
- Joel Toapanta
Fecha: 14/11/2025
"""

#Mostrar por pantalla el nombre del juego y las reglas
print ("Adivina el número secreto")
print ()
print ("Reglas del juego:")
print ("1. El Jugador1 debe ingresar un número entre el 1 y 20")
print ("2. El Jugador2 cuenta con 5 intentos para poder adivinar el número")
print ("3. Solo se puede ingresar números enteros")
print ("4. Cada vez que falle se dara una pista para saber si el número es mayor o menor")
print ()

#Solicitar al Jugador 1 que ingrese el número secreto

num_secret = 0 #Inicializamos la variable del número secreto en 0

#While se ejecutará mientras el número secreto sea 0
while num_secret == 0:
    num_jug1 = (input("Jugador 1 ingrese un número secreto: ")) #Pedir al jugador 1 que ingrese en número secreto

    #Validación del jugador 1
    digito = 1 #Inicializamos la variable en 1 (Verdadero)
    if num_jug1 == "": #Si la entrada está vacía quiere decir que no son solo son dígitos
        digito = 0 #Ponemos en 0 para indicar que no son solo dígitos
    else: #Si la entrada no está vacía debe verificar cada caracter de la cadena
        i = 0 #Lo ponenmos en cero para poder comenzar desde el primer carácter
        while i < len(num_jug1): #El ciclo se va a ejecutar mientras i sea menor que la longitud de la cadena
            if num_jug1[i] < "0" or num_jug1[i] > "9": #Si el carácter es menor que 0 o mayor que 9 entonces no es un dígito
                digito = 0 #Si el carácter no es dígito lo cambiamos a 0
            i = i + 1 #Incrementar i en 1 para pasar el siguiente carácter

    #Validar si son dígitos y que sean solo números de 1 a 20

    if digito == 1: #Verificar si el dígito es igual a 1 que son solo dígitos
        num_secret = int(num_jug1) #Convertimos la cadena a número entero usando el "int"
        if num_secret < 1 or num_secret > 20: #Condicíon para ver si el número está fuera del rango permitído
            print ("Solo ingrese números del 1 al 20")
            num_secret = 0 #Se pone de nuevo en cero para que el ciclo While continue
        else: #Condición para cuando el número esté en el rango de 1 a 20
            print ("Número secreto ingresado correctamente")
            #Prints para que baje la pantalla y no se pueda ver el número secreto
            print()
            print()
            print()
            print()
            print()
    else: #Condición para cuando no son dígitos
        print ("Solo puede ingresar números enteros")

#Solicitar al Jugador 2 adivinar el número

intentos = 5 #Se inicia la variable en 5 porque son los intentos que tiene
adivinar = 0 #Se usa para marcar en Falso (aún no se adivina) y 1 para Verdader (El número ya se adivinó)

#Ingreso de datos del Jugador 2
print ("Jugador 2 adivina el número secreto")
print ()
print ("Tienes", intentos, "intentos para poder adivinar")

#Ciclo principal para los intentos del Jugador 2
while intentos > 0 and adivinar == 0: #El ciclo continúa si "intentos" es mayor a "adivinar"
    print ("Intentos restantes:", intentos) #Muestra los intentos que tiene el jugador
    num_jug2 = (input("Ingresa un número jugador 2: ")) #Se pide que el jugador ingrese su primer intento
    digito = 1 #Se inicia en 1 para que sepa que sí es dígito
    if num_jug2 == "": #Para verificar si la entrada esta vacía
        digito = 0 #Si está vacía se cambia el dígito a cero
    else: #Si no esta vacío se va a verificar el carácter de cada cadena
        i = 0 #Se inicia en 0 para que comience desde el primer carácter
        while i < len(num_jug2): #Este ciclo recorre cada carácter de la cadena del jugador 2
            if num_jug2[i] < "0" or num_jug2[i]> "9": #Si el carácter es menor que 0 o mayor que 9 entonces no es un dígito
                digito = 0 #Si el carácter no es dígito lo cambiamos a 0
            i = i + 1 #Incrementar i en 1 para pasar el siguiente carácter

    #Validación para procesar la entrada
    if digito == 0: #Si el dígito es igual a cero entonces no son solo dígitos
        print ("Solo ingrese números") #Mensaje para decir que solo debe ingresar números
        print ("Este intento no cuenta, aun tienes", intentos, "intentos para poder adivinar") #Muestra que no se consumieron los intentos
    else:
        num_inten = int(num_jug2) #Si son solo dígitos va a convertir la cadena de texto a número entero
        if num_inten < 1 or num_inten > 20: #Condicíon para ver si el número está fuera del rango permitído
            print ("Solo puede poner número entre 1 y 20")
            print ("Este intento no cuenta, aun tienes", intentos, "intentos para poder adivinar")
        intentos = intentos - 1 #Resta 1 a los intentos restantes
        if num_inten == num_secret: #Verifica si el número ingresado por el Jugador 2 es igual al número secreto
                print ("Adivinaste el número secreto")
                adivinar = 1 #Esto hace que el ciclo While termine porque la condición anterior "adivinar == 0" será falsa
        elif num_inten > num_secret: #Condición para cuando el número ingresado es mayor al número secreto
                print ("El número secreto es menor")
        else: #Condición para cuando el número ingresado es menor al número secreto
                print ("El número secreto es mayor")


if adivinar == 0: #Esto quiere decir que se acabaron los intentos
    print ("Se acabaron los intentos, el número secreto era", num_secret) #Muestra el mensaje de que se le acabaron los intentos y muestra el número secreto
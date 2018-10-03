#funcion para operaciones aritmeticas 
def menu ():
    print ("Menu:")
    print ("1. Suma")
    print ("2. Resta")
    print ("3. Multiplicacion")
    print ("4. Division")
    print ("5. Raiz cuadrada")

def datos():
    global n1,n2
    n1 = int(input("Digite primer numero: "))
    n2 = int(input("Digite segundo numero: ")) 

def operacion ():
   if opc == 1 :
       suma = n1 + n2
       print ("El resultado de la suma es: ", suma)
   elif opc == 2 :
    	resta = n1 - n2
    	print ("El resultado de la resta es: ", resta)
   elif opc == 3 :
        multiplicacion = n1 * n2
        print ("El resultado de la multiplicacion es: ", multiplicacion)
   elif opc == 4 :
        division = n1 / n2
        print ("El resultado de la division es: ", division)  
   elif opc == 5 :
        raiz_1 = n1 ** 0.5
        raiz_2 = n2 ** 0.5
        print ("La raiz cuadrada del primer numero es: ", raiz_1)
        print ("La raiz cuadrada del segundo numero es: ", raiz_2)

datos()
menu()
opc = int(input("Elija la operacion deseada: "))
operacion ()
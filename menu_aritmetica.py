#Ejercicio menu calculadora
import os #importar librerias del sistema

os.system("cls")
print ("Menu principal")
print ("1. Sumar numeros")
print ("2. Restar numeros")
print ("3. Multiplicar numeros")
print ("4. Dividir numeros")
print ("Digite su opcion")

num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
opc = int(input("Digite la opcion a realizar: "))

if opc == 1:
	suma = num1 + num2
	print("la suma es: ",suma)
	
elif opc == 2:
	resta = num1 - num2
	print("la resta es: ",resta)
	
elif opc == 3:
	multiplicacion = num1 * num2
	print("la multiplicacion es: ",multiplicacion)
	
elif opc == 4:
	division = num1 / num2
	print("la division es: ",division)
	
else : 
	print("ingrese una opcion valida")
	

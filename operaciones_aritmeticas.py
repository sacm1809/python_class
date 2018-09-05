#Ejercicio operaciones aritmeticas
import os #importar librerias del sistema
os.system("cls")
num1 = 0
num2 = 0
opc = 0
resultado = 0
print ("Operaciones aritmeticas")
num1= int(input("ingrese el primer numero: "))
num2= int(input("ingrese el segundo numero: "))
print ("Menu de operaciones")
print ("1. Sumar numeros")
print ("2. Restar numeros")
print ("3. Multiplicar numeros")
print ("4. Dividir numeros")
opc= int(input("Digite la opcion a realizar: "))
if opc == 1 :
    resultado = num1 + num2
elif opc == 2 :
    resultado = num1 - num2    
elif opc == 3 :
    resultado = num1 * num2
elif opc == 4 :
    resultado = num1 / num2
else :
    print ("Ha digitado una opcion incorrecta!! ")
print ("el resultado de la operacion es: ",resultado)

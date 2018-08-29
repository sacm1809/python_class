num1 = 0
num2 = 0
opc = 0
resultado = 0
print ("Operaciones aritmeticas")
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
print ("Menu de operaciones: ","1.Sumar numeros ","2.Restar numeros ","3.Multiplicar numeros ","4.Dividir numeros")
opc = int(input("Digite la opcion a realizar: "))
if opc == 1 :
    print ("El resultado de la operacion es: ", num1 + num2)
elif opc == 2 :
    print ("El resultado de la operacion es: ", num1 - num2)
elif opc == 3 :
    print ("El resultado de la operacion es: ", num1 * num2)
elif opc == 4 :
    print ("EL reslutado de la operacion es: ", num1 / num2)
else:
    print ("Ha digitado una opcion incorrecta!! ")

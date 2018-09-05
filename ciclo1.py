#Numeros manuales
print ("1")
print ("2")
print ("3")
print ("4")
print ("5")
print ("6")
print ("7")
print ("8")
print ("9")
print ("10")

print ("******************")

#Numeros con ciclo while
num = 1
while num <= 10 :
    print (num)
    num = num + 1

print ("******************")

#Tabla con ciclo
num = 1
tabla= int(input("Ingrese el numero de la tabla a desarrollar: "))
while num <= 10 :
    res = tabla * num
    print (tabla, " * ", num," =", res)
    num = num + 1
    
print ("********************")

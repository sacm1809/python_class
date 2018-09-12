canus = int(input("Con cuantas personas vamos a trabajar? "))
i = 1
genm = 0
genh = 0
edades = 0
edadm = 0
edadh = 0
while i <= canus :
    edad=int(input("ingrese su edad "))
    genero=input("ingrese el genero al que pertenece (M/H): ")
    edades = edades + edad
    i = i + 1
    promedio = edades / canus
    if genero == 'M' :
        genm = genm + 1
        edadm = edadm + edad
        proedadm = edadm / genm
    elif genero == 'H' :
        genh = genh + 1
        edadh = edadh + edad
        proedadh = edadh / genh
print ("El promedio de todas las edades es: ", promedio)
print ("El numero total de mujeres es: ", genm)
print ("El numero total de hombres es: ", genh)
print ("El promedio de edades de mujeres es: ", proedadm)
print ("El promedio de edades de hombres es: ", proedadh)
print ("El numero total de personas ingresadas en el sistema es: ", canus)

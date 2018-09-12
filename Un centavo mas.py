clave0 = '1809'
intentos = 3
m = 1
saldo = 770000
while m <= intentos :
    claveus = input("Digite la clave: ")
    if clave0 == claveus :
        print ("Menú transaccional")
        print ("1. Cambiar clave")
        print ("2. Mostrar saldo")
        print ("3. Realizar retiro")
        print ("4. Salir")
        print (".:")
        opc = int(input("Seleccione opcion: "))
        if opc == 1 :
            clavenew = '0105'
            print ("Su clave nueva es ",clavenew)
            break
        elif opc == 2 :
            print ("Su saldo es de $",saldo)
            break
        elif opc == 3:
            print ("1. $10.000")
            print ("2. $20.000")
            print ("3. $50.000")
            print ("4. $100.000")
            print ("5. $200.000")
            print ("6. $400.000")
            print ("7. $600.000")
            print ("8. $1'000.000")
            subopc = int(input("Cuanto desea retirar? "))
            if subopc == 1:
                saldonew = saldo - 10000
                if saldonew < 0:
                    print ("Lo sentimos, fondos insuficientes en su cuenta")
                else :
                    print ("Ha retirado $10000")
                    print ("Saldo actual es de ",saldonew)
                break
            elif subopc == 2:
                saldonew = saldo - 20000
                if saldonew < 0:
                    print ("Lo sentimos, fondos insuficientes en su cuenta")
                else :
                    print ("Ha retirado $20000")
                    print ("Saldo actual es de ",saldonew)
                break
            elif subopc == 3:
                saldonew = saldo - 50000
                if saldonew < 0:
                    print ("Lo sentimos, fondos insuficientes en su cuenta")
                else :
                    print ("Ha retirado $50000")
                    print ("Saldo actual es de ",saldonew)
                break
            elif subopc == 4:
                saldonew = saldo - 100000
                if saldonew < 0:
                    print ("Lo sentimos, fondos insuficientes en su cuenta")
                else :
                    print ("Ha retirado $100000")
                    print ("Saldo actual es de ",saldonew)
                break
            elif subopc == 5:
                saldonew = saldo - 200000
                if saldonew < 0:
                    print ("Lo sentimos, fondos insuficientes en su cuenta")
                else :
                    print ("Ha retirado $200000")
                    print ("Saldo actual es de ",saldonew)
                break
            elif subopc == 6:
                saldonew = saldo - 400000
                if saldonew < 0:
                    print ("Lo sentimos, fondos insuficientes en su cuenta")
                else :
                    print ("Ha retirado $400000")
                    print ("Saldo actual es de ",saldonew)
                break
            elif subopc == 7:
                saldonew = saldo - 600000
                if saldonew < 0:
                    print ("Lo sentimos, fondos insuficientes en su cuenta")
                else :
                    print ("Ha retirado $600000")
                    print ("Saldo actual es de ",saldonew)
                break
            elif subopc == 8:
                saldonew = saldo - 1000000
                if saldonew < 0:
                    print ("Lo sentimos, fondos insuficientes en su cuenta")
                else :
                    print ("Ha retirado $1000000")
                    print ("Saldo actual es de ",saldonew)
                break
        elif opc == 4:
            break
        else :
            print ("opcion incorrecta")
    else :
        if m < intentos :
            print ("Clave incorrecta, le quedan",intentos - m,"intentos")
        else :
            print ("Los intentos se acabaron, su tarjeta ha sido bloqueada")
    m = m + 1

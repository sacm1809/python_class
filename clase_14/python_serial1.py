import serial, time
arduino = serial.Serial('COM5', 9600)
time.sleep(2)
rawString = arduino.readline()
print(rawString)
arduino.close()

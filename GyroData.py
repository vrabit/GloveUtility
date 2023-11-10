# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
ser.close() to close port 

Testing that updates work
"""
import csv
from serial import*

serialPort= 'COM4'
baudRate = 9600
ser = Serial(serialPort,baudRate)

def toInt(xRaw):
    flip = 65535
    tempPos = 1 << 15
    if xRaw & tempPos:
        temp =(~(xRaw) & flip) + 1
        return -temp
    else:
        return xRaw
    
def toCSV(GyroX, GyroY, GyroZ):
    with open("sensorFile.csv", 'a', newline = '') as file:
        write = csv.writer(file)
        write.writerow([GyroX,GyroY,GyroZ])
    
    
def main():
    with open("sensorFile.csv", 'w', newline = '') as file:
        write = csv.writer(file)
        header = ['GyroX', 'GyroY', 'GyroZ']
        write.writerow(header)
    
    while True:
        data = ser.readline()
        GyroXRaw = int(data[2:8].decode('utf-8'))
        GyroYRaw = int(data[10:16].decode('utf-8'))
        GyroZRaw = int(data[18:23].decode('utf-8'))
        
        GyroX = toInt(GyroXRaw)
        GyroY = toInt(GyroYRaw)
        GyroZ = toInt(GyroZRaw)
        toCSV(GyroX, GyroY, GyroZ)
        print("X: " , GyroX , "Y: " , GyroY , "Z: " , GyroZ)

        
if __name__ == "__main__":
    main()
    
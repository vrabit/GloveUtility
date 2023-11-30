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
baudRate = 19200
ser = Serial(serialPort,baudRate,timeout = 1)

def toInt(xRaw):
    flip = 65535
    tempPos = 1 << 15
    if xRaw & tempPos:
        temp =(~(xRaw) & flip) + 1
        return -temp
    else:
        return xRaw
    
def toCSV(GyroX, GyroY, GyroZ, flexThumb, flexIndex, flexMiddle, flexRing, flexPinky):
    with open("sensorFile.csv", 'a', newline = '') as file:
        write = csv.writer(file)
        write.writerow([GyroX,GyroY,GyroZ,flexThumb,flexIndex,flexMiddle,flexRing,flexPinky,2])
    
    
def main():
    with open("sensorFile.csv", 'w', newline = '') as file:
        write = csv.writer(file)
        header = ['GyroX', 'GyroY', 'GyroZ', 'Thumb', 'Index', 'Middle', 'Ring', 'Pinky', 'Gesture']
        write.writerow(header)
    
    while True:
        data = ser.readline()
        
        GyroXRaw = int(data[2:8].decode('utf-8'))
        GyroYRaw = int(data[10:16].decode('utf-8'))
        GyroZRaw = int(data[18:23].decode('utf-8'))
        flexThumb = int(data[27:33].decode('utf-8'))
        flexIndex = int(data[37:43].decode('utf-8'))
        flexMiddle = int(data[47:53].decode('utf-8'))
        flexRing = int(data[57:63].decode('utf-8'))
        flexPinky = int(data[67:73].decode('utf-8'))
        
        GyroX = toInt(GyroXRaw)
        GyroY = toInt(GyroYRaw)
        GyroZ = toInt(GyroZRaw)
        toCSV(GyroX, GyroY, GyroZ, flexThumb, flexIndex, flexMiddle, flexRing, flexPinky)
    
        print("X: " , GyroX , "Y: " , GyroY , "Z: " , GyroZ, "F1: ", flexThumb, "F2: ", flexIndex, "F3: ", flexMiddle, "F4: ", flexRing, "F5: ", flexPinky)
        
        #print(data)
        
if __name__ == "__main__":
    main()
    
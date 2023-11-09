import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


plt.style.use('bmh')
plt.figure(figsize=(10,3))


def plots():
    plt.cla()
    data = pd.read_csv('sensorFile.csv')
    time = data.index
    plt.xticks(np.arange(0, len(data)+1, 1000))
    x = data['GyroX']
    y = data['GyroY']
    z = data['GyroZ']

    plt.plot(time ,x, label='Roll', color = 'blue',linewidth = .5)
    plt.plot(time, y, label='Pitch', color = 'green',linewidth = .5)
    plt.plot(time, z, label='Yaw', color = 'red', linewidth =.5)

    plt.legend(fontsize = 'x-small')
    plt.show()

def main():
    plt.style.use('seaborn')
    plt.figure(figsize=(10,3))
    
    while True:
        plots()



if __name__ == "__main__":
    main()
    
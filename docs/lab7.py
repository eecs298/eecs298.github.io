from collections import deque
import matplotlib.pyplot as plt
import csv

def smooth(scalars, weight):  # Weight between 0 and 1
    last = scalars[0]  # First value in the plot (first timestep)
    smoothed = list()
    for point in scalars:
        smoothed_val = last * weight + (1 - weight) * point  # Calculate smoothed value
        smoothed.append(smoothed_val)                        # Save it
        last = smoothed_val                                  # Anchor the last smoothed value

    return smoothed

AVGN = 150

x = []
dqy = deque(maxlen=AVGN)

path = "progress-starpilot-idaac-20136.csv"

with open(path,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[4]))
        dqy.append(float(row[0]))

y = smooth(dqy, 0.945)

plt.plot(x[:150], y, label="label")

for i in y:
    print(i)

plt.savefig("lab7.png")
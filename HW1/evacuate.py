import csv
import matplotlib.pyplot as plt

points = []
xs = []
ys = []
# importing csv
with open('HW1data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        points.append((float(row[0]), float(row[1])))
        xs.append(float(row[0]))
        ys.append(float(row[1]))

print(points)

plt.plot(xs, ys, 'o')
plt.grid()
plt.show()
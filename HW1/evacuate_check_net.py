import csv
import matplotlib.pyplot as plt

# code that plots all possible connections between points

fig = plt.figure()
ax = fig.add_subplot()

def geom_distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

points = []
# importing csv
with open('HW1data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        points.append((float(row[0]), float(row[1])))

for p1 in points:
    for p2 in points:
        if geom_distance(p1, p2) < 1.3:
            plt.plot([p1[0], p2[0]], [p1[1], p2[1]])

ax.set_aspect('equal', adjustable='box')
plt.grid()
plt.show()
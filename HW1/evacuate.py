import csv

points = []
# importing csv
with open('HW1data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        points.append((float(row[0]), float(row[1])))

print(points)
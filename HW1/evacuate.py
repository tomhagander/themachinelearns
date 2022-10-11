import csv
import matplotlib.pyplot as plt

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.history = [] #faaaan detta får inte vara. En instans av en punkt räcker inte isåfall, eftersom vi måste kunna komma till den flera gånger.
        self.travelled_distance = 0

    def __repr__(self):
        return str(self.x) + ', ' + str(self.y)

    def __eq__(self, __o):
        return self.x == __o.x and self.y == __o.y

    def plot_history(self):
        fig = plt.figure()
        ax = fig.add_subplot()
        for p in points:
            plt.scatter(p.x, p.y, color='limegreen')
        plt.plot(*zip(*self.history), color='r')
        plt.grid()
        ax.set_aspect('equal', adjustable='box')
        # plt show at end of script

points = []
# importing csv
with open('HW1data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        points.append(Point(float(row[0]), float(row[1])))

# config
search_method = 'greedy' # 'greedy' or 'branchandbound_distance' or 'branchandbound_actions'

def geom_distance(p1, p2):
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

def cost(p1, p2):
    if search_method == 'greedy':
        return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5
    elif search_method == 'branchandbound_actions':
        return len(p1.history)
    elif search_method == 'branchandbound_distance':
        return p1.travelled_distance

def find_available_actions(current):
    visited.append(current)
    availables = []
    for point in points:
        if geom_distance(current, point) < 1.3 and point not in visited: # skips all visited
            #creating history for new point
            point.history = current.history.copy()
            point.history.append((point.x, point.y))
            point.travelled_distance = current.travelled_distance + geom_distance(current, point)
            #adding new point to availables
            availables.append(point)
    return availables 

I = points[0] #start at (0,0)
I.history = [(0,0)]
G = points[-1] #goal
frontier = [I]
visited = []
success = False

while not success:
    # pick best point from frontier using cost function defined above
    min_cost = float('inf')
    best_point_idx = None
    for idx, point in enumerate(frontier):

        if geom_distance(point, G) == 0: #checks if terminal
            # terminal
            print('terminal')
            print(point)
            print(point.history)
            point.plot_history()
            print(len(point.history))
            success = True
            break

        elif cost(point, G) < min_cost: #checks if point is better than points before in frontier
            min_cost = cost(point, G)
            best_point_idx = idx
    best_point = frontier.pop(best_point_idx)

    availables = find_available_actions(best_point)

    # adding availables to frontier. Maybe make frontier into a min_heap here? Current implementation works too, dont know which is faster
    frontier = frontier + availables

plt.show()
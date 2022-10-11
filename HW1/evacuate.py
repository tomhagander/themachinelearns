import csv
import matplotlib.pyplot as plt

class Point():
    def __init__(self, x, y, history=[]):
        self.x = x
        self.y = y
        self.history = history
        self.history.append((self.x, self.y))
        self.travelled_distance = 0

    def __repr__(self):
        return str(self.x) + ', ' + str(self.y)

    def __eq__(self, __o):
        return self.x == __o.x and self.y == __o.y

    def plot_history(self):
        fig = plt.figure()
        ax = fig.add_subplot()
        for p in coords:
            plt.scatter(p[0], p[1], color='limegreen')
        plt.plot(*zip(*self.history), color='r')
        plt.grid()
        plt.title(search_method)
        ax.set_aspect('equal', adjustable='box')
        # plt show at end of script

coords = []
# importing csv
with open('HW1data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        coords.append((float(row[0]), float(row[1])))

# config
search_method = 'greedy' # 'greedy' or 'branchandbound_distance' or 'branchandbound_actions'

def geom_distance(point, coord):
    return ((point.x - coord[0])**2 + (point.y - coord[1])**2)**0.5

def cost(point, goal_coord):
    if search_method == 'greedy':
        return ((point.x - goal_coord[0])**2 + (point.y - goal_coord[1])**2)**0.5
    elif search_method == 'branchandbound_actions':
        return len(point.history)
    elif search_method == 'branchandbound_distance':
        return point.travelled_distance
    else:
        print('invalid input')

def find_available_actions(current):
    visited.append((current.x, current.y))
    availables = []
    for coord in coords:
        if geom_distance(current, coord) < 1.3 and coord not in visited: # skips all visited
            #creating history for new point
            point = Point(coord[0], coord[1], current.history.copy())
            point.travelled_distance = current.travelled_distance + geom_distance(current, coord)
            #adding new point to availables
            availables.append(point)
    return availables 

I = Point(coords[0][0], coords[0][1]) #start at (0,0)
I.history = [(0,0)]
G_coord = coords[-1] #goal
frontier = [I]
visited = []
success = False

while not success:
    # pick best point from frontier using cost function defined above
    min_cost = float('inf')
    best_point_idx = None
    for idx, point in enumerate(frontier):

        if geom_distance(point, G_coord) == 0: #checks if terminal
            # terminal
            print('terminal')
            print(point)
            print(point.history)
            point.plot_history()
            print(len(point.history))
            success = True
            break

        elif cost(point, G_coord) < min_cost: #checks if point is better than points before in frontier
            min_cost = cost(point, G_coord)
            best_point_idx = idx
    best_point = frontier.pop(best_point_idx)

    availables = find_available_actions(best_point)

    # adding availables to frontier. Maybe make frontier into a min_heap here? Current implementation works too, dont know which is faster
    frontier = frontier + availables

plt.show()
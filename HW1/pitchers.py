
# breadth first and depth first search for solutions to the problem with two pitchers

# actions: 
# - Fill p3 from tap -> p3 = 3
# - Pour p3 to p5 until p5 full
# - Pour p5 to p3 until p3 full
# - Empty p3
# - Empty p5

# breadth first - explore oldest state in frontier
# depth first - explore newest state in frontier

# unresolved: Take goal as soon as its seen?
# Add states already in frontier to frontier?

class State:
    def __init__(self, p3, p5, history):
        self.p3 = p3
        self.p5 = p5
        self.history = history

    def __eq__(self, __o):
        return (self.p3 == __o.p3) and (self.p5 == __o.p5)

    def __repr__(self):
        repr = 'p3: ' + str(self.p3) + ', p5: ' + str(self.p5) + ', hist: '
        for h in self.history:
            repr = repr + str(h)
        return repr

    def take_action(self, idx):
        history = self.history.copy()
        if idx == 1: #fill p3
            p3 = 3
            p5 = self.p5
            history.append(1)
            return State(p3, p5, history)

        elif idx == 2: #pour p3 to p5
            if (5 - self.p5 >= self.p3):
                p3 = 0
                p5 = self.p5 + self.p3
            else:
                p5 = 5
                p3 = self.p3 - (5 - self.p5)
            history.append(2)
            return State(p3, p5, history)

        elif idx == 3: #pour p5 to p3
            if (3 - self.p3 >= self.p5):
                p3 = self.p3 + self.p5
                p5 = 0
            else:
                p3 = 3
                p5 = self.p5 - (3 - self.p3)
            history.append(3)
            return State(p3, p5, history)

        elif idx == 4: #empty p3
            p3 = 0
            p5 = self.p5
            history.append(4)
            return State(p3, p5, history)

        elif idx == 5: # empty p5
            p3 = self.p3
            p5 = 0
            history.append(5)
            return State(p3, p5, history)

    def isTerminal(self):
        return self.p5 == 4


# configureable stuff
s0 = State(0, 0, [])
search_method = 'depth' # 'depth' or 'breadth' or 'Astar'
print(search_method)
success = False
goal_seq = []
frontier = [s0]
visited = [s0]

ctr = 0
while not success:
    ctr += 1
    # pick state from frontier
    print(frontier)
    if search_method == 'depth':
        s = frontier.pop()
    elif search_method == 'breadth':
        s = frontier.pop(0)
    elif search_method == 'Astar':
        min_cost = float('inf') # number larger than all others
        best_idx = None # will be assigned value if frontier not empty
        for i, candidate in enumerate(frontier):
            travelled_dist = len(candidate.history) # chosen to be how many times pitchers have been moved
            flight_dist = abs(candidate.p5 - 4) # chosen to be difference to 4 in liters of 5L pitcher
            if travelled_dist + flight_dist < min_cost:
                min_cost = travelled_dist + flight_dist
                best_idx = i
        s = frontier.pop(best_idx)

    # expanding (results differ for greedy if range is reversed or not, which is to be expected)
    for action_nbr in reversed(range(1, 6)): #checking all actions 1-5 to see if they are (1) terminal or (2) viable
        s_new = s.take_action(action_nbr)
        if s_new.isTerminal():
            success = True
            goal_seq = s_new.history
            print('terminal')
            break
        elif s_new not in visited:
            visited.append(s_new)
            frontier.append(s_new)

print('history')
print(goal_seq)
print(ctr)
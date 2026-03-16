from simpleai.search import SearchProblem, hill_climbing
from tsp_proiect.src.utils.backtracking import citeste_matrice
import itertools

class TSPHillClimbing(SearchProblem):
    orase : list
    n: int
# [[1,2,3]]

    def __init__(self, orase, n, initial):
        super().__init__(initial_state=initial)
        self.orase = orase
        self.n = n

    def getVecini(self, state):
       actions = []
       for i in range(1, len(state) - 1):
           for j in range(i+1, len(state)):
               actions.append((i,j))

       return actions

    def actions(self, state):
        if len(state) < self.n+1:
            return self.getVecini(state)
        else:
            return []


    def result(self, state, action): # (1,2)
        new_state = list(state)
        new_state[action[0]], new_state[action[1]] = new_state[action[1]], new_state[action[0]]
        print(self.value(state), state, "->", self.value(new_state), new_state, "action:", action)

        return tuple(new_state)

    def value(self, state):
        dist = 0
        for i in range(len(state) - 1): # 2 1 3 4 0 2
            dist += orase[state[i]][state[i+1]]
        dist += orase[state[-1]][state[0]]
        print("distanta in value", dist)
        return dist

    # def is_goal(self, state):
    #     return len(state) == self.n
    #
    # def cost(self, state, action, state2):
    #     orasCur = self.orase[state[-1]]
    #     cost = orasCur[action]
    #     return cost

    # def heuristic(self, state):
    #     # how far are we from the goal? O
    #     wrong = sum([1 if state[i] == state[-1] else 0
    #                 for i in range(len(state)-1)])
    #     missing = self.n - len(state)
    #     return wrong + missing

# print()
n, orase = citeste_matrice("in.txt")
# print(orase)
problem = TSPHillClimbing(n=n, orase=orase, initial=(0,1,2,3,4))
result = hill_climbing(problem)

print(result.state)
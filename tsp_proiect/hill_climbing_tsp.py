import random

from simpleai.search import SearchProblem, hill_climbing, hill_climbing_random_restarts

class TSPHillClimbing(SearchProblem):
    def __init__(self, orase, n):
        super().__init__()
        self.orase = orase
        self.n = n

        self.actiuni = []
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                self.actiuni.append((i, j))

    def getVecini(self, state):
       actions = []
       for i in range(1, len(state) - 1):
           for j in range(i+1, len(state)):
               actions.append((i,j))

       return actions

    def actions(self, state):
        if len(state) < self.n+1:
            return self.actiuni
            # return self.getVecini(state)
        else:
            return []


    def result(self, state, action): # (1,2)
        new_state = list(state)
        new_state[action[0]], new_state[action[1]] = new_state[action[1]], new_state[action[0]]
        # print(self.value(state), state, "->", self.value(new_state), new_state, "action:", action)

        return tuple(new_state)

    def value(self, state):
        dist = 0
        for i in range(len(state) - 1): # 2 1 3 4 0 2
            dist += self.orase[state[i]][state[i+1]]
        dist += self.orase[state[-1]][state[0]]
        # print("distanta in value", dist)
        return -dist

    def generate_random_state(self):
        initial_state = [i for i in range(1, self.n)]
        random.shuffle(initial_state)
        return [0] + initial_state

def rezolva_hill_climbing(orase, nr_orase):
    problem = TSPHillClimbing(n=nr_orase, orase=orase)
    result = hill_climbing_random_restarts(problem, restarts_limit=1)

    return result, result.value
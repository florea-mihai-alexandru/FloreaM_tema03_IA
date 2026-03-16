from simpleai.search import SearchProblem, astar
from tsp_proiect.src.utils.backtracking import citeste_matrice
class TSPHillClimbing(SearchProblem):
    orase : list
    n: int
# [[1,2,3]]

    def __init__(self, orase, n, initial):
        super().__init__(initial_state=initial)
        self.orase = orase
        self.n = n

    def getVecini(self, orasCur, state):
        vec = []
        for oras in self.orase[orasCur]:
            if oras != 0:
                ok=True
                for i in state:
                    if oras == i:
                        ok=False
                if ok:
                    vec.append(oras)
        return vec


    def actions(self, state):
        if len(state) < self.n+1:
            return self.getVecini(state[-1], state)
        else:
            return []

    def result(self, state, action):
        return state.append(action)

    def is_goal(self, state):
        return len(state) == self.n

    def cost(self, state, action, state2):
        orasCur = self.orase[state[-1]]
        cost = orasCur[action]
        return cost

    def heuristic(self, state):
        # how far are we from the goal? O
        wrong = sum([1 if state[i] == state[-1] else 0
                    for i in range(len(state)-1)])
        missing = self.n - len(state)
        return wrong + missing

# print()
n, orase = citeste_matrice("in.txt")
problem = TSPHillClimbing(n=n, orase=orase, initial=[0])
result = astar(problem)

print(result.state)
print(result.path())
import time

from instance import *
from solution import *
from constructives import *
from improvements import *
import time

random.seed(13)

path = "instances/Path15_Star50.txt"
instance = readInstance(path)
alpha = -1
ini = time.time()
bestOF = float("Inf")
for i in range(100):
    #print("Solution "+str(i))
    #solution = randomConstruct(instance)
    #solution = greedyConstruct(instance)
    #solution = graspConstructive(instance, alpha)
    #solution = graspConstructiveEfficient(instance, alpha)
    #solution = graspConstructiveEfficient2(instance, alpha)
    solution = graspConstructiveEfficientRandomGreedy(instance, alpha)
    print(solution['of'], end=" -> ")
    localSearch(solution)
    print(solution['of'])
    bestOF = min(solution['of'], bestOF)
    #print(str(solution['selected'])+" -> "+str(solution['of']))
secs = time.time() - ini
print("Time: "+str(secs)+" s")
print("OF: "+str(bestOF))

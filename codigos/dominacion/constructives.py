from solution import *
from instance import *
import random

def randomConstruct(instance):
    solution = createSolution(instance)
    cl = []
    for i in range(instance['n']):
        if i not in solution['selected']:
            cl.append(i)
    while not isFeasible(solution):



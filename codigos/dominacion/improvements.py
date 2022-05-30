from instance import *
from solution import *
import copy

def localSearch(solution):
    improve = True
    while improve:
        improve = tryImprove(solution)

def tryImprove(solution):
    n = solution['instance']['n']
    oldOf = solution['of']
    for u in range(n):
        if u not in solution['selected']:
            addNode(solution, u)
            removed = removeNotNecessary(solution, u)
            evaluate(solution)
            if solution['of'] < oldOf:
                return True
            removeNode(solution, u)
            for rem in removed:
                addNode(solution, rem)
    return False
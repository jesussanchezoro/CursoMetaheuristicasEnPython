from instance import *
from solution import *
import random


def randomConstruct(instance):
    solution = createSolution(instance)
    cl = list(range(instance['n']))
    while not isFeasible(solution):
        idx = random.randint(0, len(cl)-1)
        node = cl[idx]
        del cl[idx]
        if node not in solution['selected']:
            addNode(solution, node)
    evaluate(solution)
    return solution

def greedyFunction(solution, u):
    newDominated = 0
    if solution['dominated'][u] == 0:
        newDominated += 1
    for v in solution['instance']['l'][u]:
        if solution['dominated'][v] == 0:
            newDominated += 1
    return newDominated


def greedyConstruct(instance):
    solution = createSolution(instance)
    cl = list(range(instance['n']))
    while not isFeasible(solution):
        greedy = -1
        selected = -1
        for i in range(len(cl)):
            if cl[i] not in solution['selected']:
                g = greedyFunction(solution, cl[i])
                if g > greedy:
                    greedy = g
                    selected = i
        addNode(solution, selected)
        evaluate(solution)
    return solution


def createCL(solution):
    instance = solution['instance']
    cl = []
    for u in range(instance['n']):
        if u not in solution['selected']:
            cl.append(u)
    return cl


def evalGminGmax(solution, cl):
    gmin = float("Inf")
    gmax = 0
    for c in cl:
        g = greedyFunction(solution, c)
        gmin = min(gmin, g)
        gmax = max(gmax, g)
    return gmin, gmax


def createRCL(solution, cl, mu):
    rcl = []
    for c in cl:
        if greedyFunction(solution, c) >= mu:
            rcl.append(c)
    return rcl

def graspConstructive(instance, alpha):
    solution = createSolution(instance)
    cl = createCL(solution)
    idx = random.randint(0,len(cl)-1)
    first = cl[idx]
    del cl[idx]
    addNode(solution, first)
    while not isFeasible(solution):
        gmin, gmax = evalGminGmax(solution, cl)
        mu = gmax - alpha * (gmax - gmin)
        rcl = createRCL(solution, cl, mu)
        selected = rcl[random.randint(0, len(rcl)-1)]
        addNode(solution, selected)
        cl.remove(selected)
    removeNotNecessary(solution)
    evaluate(solution)
    return solution


def createCLEfficient(solution):
    cl = []
    gmin = float("Inf")
    gmax = 0
    for u in range(solution['instance']['n']):
        if u not in solution['selected']:
            g = greedyFunction(solution, u)
            cl.append([u, g])
            gmin = min(gmin, g)
            gmax = max(gmax, g)
    return cl, gmin, gmax


def graspConstructiveEfficient(instance, alphaInput):
    alpha = alphaInput if alphaInput >= 0 else random.random()
    solution = createSolution(instance)
    first = random.randint(0, instance['n']-1)
    while first in solution['selected']:
        first = (first + 1) % instance['n']
    addNode(solution, first)
    cl, gmin, gmax = createCLEfficient(solution)
    rcl = [0] * instance['n']
    limitRCL = 0
    while not isFeasible(solution):
        mu = gmax - alpha * (gmax - gmin)
        limitRCL = 0
        for i in range(len(cl)):
            c = cl[i]
            if c[1] >= mu:
                rcl[limitRCL] = i
                limitRCL += 1
        idxSelected = rcl[random.randint(0, limitRCL-1)]
        selected = cl[idxSelected]
        del cl[idxSelected]
        addNode(solution, selected[0])
        gmax = 0
        gmin = float("Inf")
        for c in cl:
            c[1] = greedyFunction(solution, c[0])
            gmax = max(gmax, c[1])
            gmin = min(gmin, c[1])
    removeNotNecessary(solution)
    evaluate(solution)
    return solution



def graspConstructiveEfficient2(instance, alpha):
    solution = createSolution(instance)
    first = random.randint(0, instance['n'])
    while first in solution['selected']:
        first = (first + 1) % instance['n']
    addNode(solution, first)
    cl, gmin, gmax = createCLEfficient(solution)
    while not isFeasible(solution):
        mu = gmax - alpha * (gmax - gmin)
        idxSelected = random.randint(0, len(cl)-1)
        while cl[idxSelected][1] < mu:
            idxSelected = (idxSelected + 1) % len(cl)
        selected = cl[idxSelected]
        del cl[idxSelected]
        addNode(solution, selected[0])
        gmax = 0
        gmin = float("Inf")
        for c in cl:
            c[1] = greedyFunction(solution, c[0])
            gmax = max(gmax, c[1])
            gmin = min(gmin, c[1])
    removeNotNecessary(solution)
    evaluate(solution)
    return solution


def createCLEfficientRandomGreedy(solution):
    cl = []
    for u in range(solution['instance']['n']):
        if u not in solution['selected']:
            cl.append(u)
    return cl

def graspConstructiveEfficientRandomGreedy(instance, alphaInput):
    alpha = alphaInput if alphaInput >= 0 else random.random()
    solution = createSolution(instance)
    first = random.randint(0, instance['n']-1)
    while first in solution['selected']:
        first = (first + 1) % instance['n']
    addNode(solution, first)
    cl = createCLEfficientRandomGreedy(solution)
    while not isFeasible(solution):
        evals = int(len(cl) * alpha)
        idxSelected = -1
        bestG = 0
        for i in range(evals):
            idx = random.randint(0, len(cl)-1)
            g = greedyFunction(solution, cl[idx])
            if g > bestG:
                bestG = g
                idxSelected = idx
        selected = cl[idxSelected]
        del cl[idxSelected]
        addNode(solution, selected)
    removeNotNecessary(solution)
    evaluate(solution)
    return solution















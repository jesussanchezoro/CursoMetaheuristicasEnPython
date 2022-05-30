

def createSolution(instance):
    solution = {}
    solution['instance'] = instance
    solution['selected'] = set()
    solution['of'] = 0
    solution['dominated'] = [0] * instance['n']
    solution['nDominated'] = 0
    addSupportNodes(solution)
    return solution


def addSupportNodes(solution):
    solution['support'] = set()
    for u in range(solution['instance']['n']):
        if len(solution['instance']['l'][u]) == 1:
            addNode(solution, solution['instance']['l'][u][0])
            solution['support'].add(solution['instance']['l'][u][0])


def evaluate(solution):
    solution['of'] = len(solution['selected'])


def addNode(solution, u):
    solution['selected'].add(u)
    if solution['dominated'][u] == 0:
        solution['nDominated'] += 1
    solution['dominated'][u] += 1
    for v in solution['instance']['l'][u]:
        if solution['dominated'][v] == 0:
            solution['nDominated'] += 1
        solution['dominated'][v] += 1


def removeNode(solution, u):
    solution['selected'].remove(u)
    solution['dominated'][u] -= 1
    if solution['dominated'][u] == 0:
        solution['nDominated'] -= 1
    for v in solution['instance']['l'][u]:
        solution['dominated'][v] -= 1
        if solution['dominated'][v] == 0:
            solution['nDominated'] -= 1


def isFeasible(solution):
    return solution['nDominated'] == solution['instance']['n']


def isNecessary(solution, u):
    if solution['dominated'][u] == 1:
        return True
    for v in solution['instance']['l'][u]:
        if solution['dominated'][v] == 1:
            return True
    return False


def removeNotNecessary(solution, u = -1):
    l = []
    removed = True
    while removed:
        removed, node = checkNotNecessary(solution, u)
        if removed:
            l.append(node)
    return l


def checkNotNecessary(solution, exc = -1):
    for u in solution['selected']:
        if u != exc and not isNecessary(solution, u):
            removeNode(solution, u)
            return True, u
    return False, -1
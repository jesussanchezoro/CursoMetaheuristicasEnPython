
def addSupportNodes(solution):
    n = solution['instance']['n']
    for u in range(n):
        if len(solution['instance']['l'][u]) == 1:
            addNode(solution, solution['instance']['l'][0])


def createSolution(instance):
    solution = {}
    solution['instance'] = instance
    solution['selected'] = []
    solution['covered'] = set()
    solution['coveredBy'] = []
    for i in range(instance['n']):
        solution['coveredBy'].append(set())
    addSupportNodes(solution)
    return solution


def evaluate(solution):
     return len(solution['selected'])


def addNode(solution, node):
    solution['selected'].append(node)
    for adj in solution['instance']['l'][node]:
        solution['covered'].add(adj)
        solution['coveredBy'][adj].add(node)


def removeNode(solution, node):
    solution['selected'].remove(node)
    for adj in solution['instance']['l'][node]:
        solution['coveredBy'][adj].remove(node)
        if not solution['coveredBy'][adj]:
            solution['covered'].remove(adj)


def isFeasible(solution):
    return len(solution['covered']) == solution['instance']['n']
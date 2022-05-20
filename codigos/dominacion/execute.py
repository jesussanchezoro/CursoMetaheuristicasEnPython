from instance import *
from solution import *



if __name__ == '__main__':
    path = "/Users/jesus.sanchezoro/IdeaProjects/instancias/dominatic/Grid/Grid 2x2.txt"
    instance = readInstance(path)
    # print(instance)
    solution = createSolution(instance)
    addNode(solution, 1)
    addNode(solution, 3)
    removeNode(solution, 1)
    print(solution['selected'])
    print(solution['covered'])
    print(solution['coveredBy'])


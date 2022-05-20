
def readInstance(path):
    instance = {}
    with open("instances/Grid 2x2.txt", "r") as f:
        n = int(f.readline().strip())
        f.readline()
        instance['n'] = n
        instance['m'] = []
        instance['l'] = []
        for _ in range(n):
            instance['m'].append([0] * n)
            instance['l'].append([])
        for i in range(n):
            line = list(map(int, f.readline().strip().split()))
            for j in range(len(line)):
                if line[j] == 1:
                    instance['m'][i][j] = 1
                    instance['m'][j][i] = 1
                    instance['l'][i].append(j)
    return instance
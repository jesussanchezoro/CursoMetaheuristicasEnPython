numbers = list(map(int, input().strip().split()))
mean = 0
for n in numbers:
    mean += n
print("La media es " + str(mean/len(numbers)))
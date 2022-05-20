numbers = list(map(int, input().strip().split()))
n = int(input().strip())

count = 0
for number in numbers:
    if n == number:
        count += 1
print("El " + str(n) + " aparece " + str(count) + " veces")
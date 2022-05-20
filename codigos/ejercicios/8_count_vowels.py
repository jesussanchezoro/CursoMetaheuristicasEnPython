sentence = input().strip()
vowels = 'aeiouAEIOU'
count = 0
for s in sentence:
    if s in vowels:
        count += 1
print("Tiene " + str(count) + " vocales")
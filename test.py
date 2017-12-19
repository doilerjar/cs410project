import random as rand

rand_set = []

for i in range(500):
    found = False
    while not found:
        rand_number = rand.randint(1, 50000)
        if len(rand_set) == 0:
            rand_set.append(rand_number)
            found = True
        else:
            if rand_number not in rand_set:
                rand_set.append(rand_number)
                found = True

print(rand_set)


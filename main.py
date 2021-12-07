totalTime = 0

file = open("Pullups.txt")

for line in file:
    dayTime = int(line)
    if 1 <= dayTime <= 13:
        totalTime += dayTime
    print("activity today:", dayTime)

print(totalTime)

file.close()

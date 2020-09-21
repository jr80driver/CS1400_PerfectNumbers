# Jacob Smith
# A01476417
# Assn8
# This program will determine the four perfect numbers under 10,000

import time
start = time.time()

perNum = 0
iteration = 0
for i in range(2, 10000):
    if perNum == 4:
        break
    else:
        if i % 2 == 0 and i % 5 != 0:
            totalSum = 1
            bigNum = i
            for j in range(2, bigNum):
                iteration += 1
                if bigNum % j == 0:
                    totalSum += j
            if totalSum == i:
                perNum += 1
                print(i)
print("Total iterations of the inner loop: ", iteration)
end = time.time()
runtime = round((end - start), 2)
print("Total runtime: ", runtime)



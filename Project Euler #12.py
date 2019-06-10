import time
start = time.time()
sums = [1]
primelist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

def triangle_number(w):
    numbers = [1]
    for y in range(2,w+1):
        sums.append(y+sum(numbers))
        numbers.append(y)
    print(sums)

triangle_number(12)

import time
start = time.time()

def triangle_number(w):
    numbers = []
    sums = []
    for y in range(1,w):
            for x in range(1,y+1):
                numbers.append(x)
            sums.append((sum(numbers)))
            numbers.clear()
    print(sums)

triangle_number(10)

end = time.time()
print(end - start)

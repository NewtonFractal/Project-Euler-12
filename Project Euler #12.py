import time
start = time.time()
sums = []

def triangle_number(w):
    numbers = []
    for y in range(1,w):
            for x in range(1,y+1):
                numbers.append(x)
            sums.append((sum(numbers)))
            numbers.clear()
    print(sums)

triangle_number(10)

end = time.time()
print(end - start)

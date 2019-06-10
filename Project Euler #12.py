import time
numbers = []
start = time.time()
def triangle_number(y):
    for x in range(1,y):
        numbers.append(x)
    print(sum(numbers))

triangle_number(5)

end = time.time()
print(end - start)

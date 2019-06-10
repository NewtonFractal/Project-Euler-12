import time
import math

start = time.time()
sums = []
divisors = []


def triangle_number(w):
    for y in range(100, w + 1):
        sums.append(int(((y + 1) * y) / 2))


triangle_number(1000000)

end = time.time()
print(end - start)


def Highly_divisible_triangular_number():
    Done = False
    for x in sums:
        for y in range(2, x):
            if x % y == 0:
                divisors.append(y)
                if len(divisors) == 498:
                    Done = True
                    print(x)
                    break
        divisors.clear()
        if Done == True:
            break


Highly_divisible_triangular_number()
end = time.time()
print(end - start)

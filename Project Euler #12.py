import time
import math
start = time.time()
sums = []
divisors = []

def triangle_number(w):
    for y in range(2,w+1):
        sums.append(int(((y+1)*y)/2))
    print(sums)

triangle_number(50)

end = time.time()
print(end - start)

def Highly_divisible_triangular_number():
    for x in sums:
        for y in range(2,x):
            if x % y == 0:
                divisors.append(y)
             
Highly_divisible_triangular_number()
print(Factors)
end = time.time()
print(end - start)

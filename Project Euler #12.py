import time
import math
start = time.time()
sums = [1]
Factors = []
primelist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
primelist2 = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

def triangle_number(w):
    for y in range(2,w+1):
        sums.append(int(((y+1)*y)/2))
    print(sums)

triangle_number(50)

end = time.time()
print(end - start)

def Highly_divisible_triangular_number():
    for z in sums:
        for x in primelist:
            factor = True
            while factor == True:
                if z % x != 0:
                    factor = False
                    break
                Factors.append(x)
                z = int(z/x)
            if x > z+ 1:
                break
        for y in range(103, z + 1, 2):
            prime = True
            for x in primelist2:
                if y % x == 0:
                    prime = False
                    break
                if x > math.sqrt(y):
                    break
            if prime == True:
                primelist2.append(y)
                factor2 = True
                while factor2 == True:
                    if z % y != 0:
                        factor2 = False
                        break
                    Factors.append(y)
                    z = number / y
                    if y > z + 1:
                        break
                if y > z + 1:
                    break
            if y > z+ 1:
                break

Highly_divisible_triangular_number()
print(Factors)
end = time.time()
print(end - start)

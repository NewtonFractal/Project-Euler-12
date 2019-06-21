import math
import time

start = time.time()
Answer =[]

def Highly_divisible_triangular_number(number):
    factors = []
    for x in range(1, int(math.sqrt(number)+1)):
        if number % x == 0:
            factors.append(number / x)
            factors.append(x)
        if len(factors) > 500:
            Answer.append(number)
            print(number)
            break


def Triangle_number_generator(upper_bound):
    for x in range(1, upper_bound):
        if len(Answer) == 1:
            break
        Highly_divisible_triangular_number((x * (x + 1)) / 2)

Triangle_number_generator(100000)

end = time.time()
print(end - start)

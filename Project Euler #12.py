import math
import time

Answer =[]
start = time.time()

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

def Triangle_number_generator(lower_bound,upper_bound):
    for x in range(lower_bound, upper_bound):
        if len(Answer) == 1:
            break
        Highly_divisible_triangular_number((x * (x + 1)) / 2)

def lower_bound_finder(sum):
    Triangle_number_generator(int(((math.sqrt(8*sum+1)-1)/2)),34673462344326)

lower_bound_finder(2*3*5*7*11*13*17*19*5)

end = time.time()
print(end - start)

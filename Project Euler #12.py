import math
import time
Answer =[]
start = time.time()

def Highly_divisible_triangular_number(number):
    factors = [1]
    for x in range(2, int(math.sqrt(number)+1)):
        if number % x == 0:
            factors.append(number/x)
            factors.append(x)
    if len(factors) > 500:
        Answer.append(number)
        print(number)

def Triangle_number_generator(lower_bound,upper_bound):
    for x in range(lower_bound, upper_bound):
        if len(Answer) == 1:
            break
        Highly_divisible_triangular_number((x *(x+1))/2)

def lower_bound_finder(sum):
    Triangle_number_generator(int(((math.sqrt(8*sum+1)-1)/2)),34673462)

lower_bound_finder((2**4)*(3**4)*(5**4)*(7)*(11))

end = time.time()
print(end - start)

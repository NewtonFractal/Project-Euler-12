import time
start = time.time()
sums = [1]
primelist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

def triangle_number(w):
    for y in range(2,w+1):
        sums.append(int(((y+1)*y)/2))
    print(sums)

triangle_number(10000)

end = time.time()
print(end - start)

def triangle_divisors(LCM):
    for x in sums:
        for y in primelist:
            while x > y:
                y = y*x
                if x > y:
                    LCM = LCM *x
                else:
                    continue
                

                
triangle_divisors(1)

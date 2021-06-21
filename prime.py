import math
import multiprocessing
import time

def check_prime(N):
    arr = [True]*N
    for num in range(N):
        if num<2:
            arr[num] = False
        elif num>2:
            for j in range(2, math.ceil(math.sqrt(num))+1):
                if num%j==0:
                    arr[num] = False
                    break
    return arr

def check_prime_multi(num):
    if num<2:
        return num, False
    elif num==2:
        return num, True
    else:
        for j in range(2, math.ceil(math.sqrt(num))+1):
                if num%j==0:
                    return num, False
    return num, True

if __name__ == "__main__":
    N = 2 * 10**6

    # singleprocessing
    st = time.time()
    results = check_prime(N)
    print(results[:30])
    en = time.time()
    print("time taken = ", en-st)

    # multiprocessing
    st = time.time()
    num_arr = range(N)
    results = []
    with multiprocessing.Pool(processes=10) as pool:
        results = pool.map(check_prime_multi, num_arr)
    pool.close()
    print(results[:30])
    en = time.time()
    print("time taken = ", en-st)

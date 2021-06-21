import multiprocessing
import  time

def counter1(num):
    cnt = 0
    for _ in range(num):
        cnt += 1
    print("counter1 done!")

def counter2(num):
    cnt = 0
    for _ in range(0, num, 2):
        cnt += 1
    print("counter2 done!")

if __name__ == "__main__":
    N = 2 * 10**8

    # singleprocessing
    st = time.time()
    counter1(N)
    counter2(N)
    en = time.time()
    print("time taken = ", en-st)

    # multiprocessing
    st = time.time()
    p1 = multiprocessing.Process(target=counter1, args=(N, ))
    p2 = multiprocessing.Process(target=counter2, args=(N, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    en = time.time()
    print("time taken = ", en-st)
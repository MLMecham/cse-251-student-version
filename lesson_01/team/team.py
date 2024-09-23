"""
Course: CSE 251 
Lesson: L01 Team Activity
File:   team.py
Author: Mitchell Mecham

Purpose: Find prime numbers

Instructions:

- Don't include any other Python packages or modules
- Review and follow the team activity instructions (team.md)
"""

from datetime import datetime, timedelta
import threading
import random

# Include cse 251 common Python files
from cse251 import *

# Global variable for counting the number of primes found
prime_count = 0
numbers_processed = 0

def is_prime(n):
    # global numbers_processed
    # numbers_processed += 1

    """
    Primality test using 6k+-1 optimization.
    From: https://en.wikipedia.org/wiki/Primality_test
    """

    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def make_thread(start1, lock_prime, lock_processed):
    global prime_count
    global numbers_processed
    lock = threading.Lock()
    start = 10000000000 + start1
    range_count = 10000
    for i in range(start, start + range_count):
        if is_prime(i):
            with lock_prime:
                prime_count += 1
            print(i, end=', ', flush=True)
        with lock_prime:
            numbers_processed += 1
    print(flush=True)
    ...


if __name__ == '__main__':
    log = Log(show_terminal=True)
    log.start_timer()

    lock_prime = threading.Lock()
    lock_processed = threading.Lock()

    # TODO 1) Get this program running
    # TODO 2) move the following for loop into 1 thread
    
    #t1 = threading.Thread(target=make_thread, args=(0,0))
    #t1.start()
    #t1.join()
    # TODO 3) change the program to divide the for loop into 10 threads

    t1 = threading.Thread(target=make_thread, args=(0, lock_prime, lock_processed))
    t2 = threading.Thread(target=make_thread, args=(10000, lock_prime,lock_processed))
    t3 = threading.Thread(target=make_thread, args=(20000, lock_prime,lock_processed))
    t4 = threading.Thread(target=make_thread, args=(30000, lock_prime,lock_processed))
    # t5 = threading.Thread(target=make_thread, args=(0,40000))
    # t6 = threading.Thread(target=make_thread, args=(0,50000))
    # t7 = threading.Thread(target=make_thread, args=(0,60000))
    # t8 = threading.Thread(target=make_thread, args=(0,70000))
    # t9 = threading.Thread(target=make_thread, args=(0,80000))
    # t10 = threading.Thread(target=make_thread, args=(0,90000))
    # t10 = threading.Thread(target=make_thread, args=(0,100000))
    

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    # t5.start()
    # t6.start()
    # t7.start()
    # t8.start()
    # t9.start()
    # t10.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    # t5.join()
    # t6.join()
    # t7.join()
    # t8.join()
    # t9.join()
    # t10.join()
    # TODO 4) change range_count to 100007.  Does your program still work?  Can you fix it?
    # Question: if the number of threads and range_count was random, would your program work?

    # start = 10000000000
    # range_count = 100000
    # for i in range(start, start + range_count):
    #     if is_prime(i):
    #         prime_count += 1
    #         print(i, end=', ', flush=True)
    # print(flush=True)

    # Should find 4306 primes
    log.write(f'Numbers processed = {numbers_processed}')
    log.write(f'Primes found      = {prime_count}')
    log.stop_timer('Total time')


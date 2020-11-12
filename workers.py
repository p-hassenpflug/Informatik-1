import multiprocessing
import random

def mysort(N):
    "Create a list of random numbers of length N, and return a sorted list"

    # Create random list 
    x = random.sample(range(0, N), N) 

    # Print process identifier (just out of interest)
    print("Process id: {}".format(multiprocessing.current_process()))
    
    # Return sorted list of numbers
    return sorted(x)

def worker(x):
    y = x * x
    return y

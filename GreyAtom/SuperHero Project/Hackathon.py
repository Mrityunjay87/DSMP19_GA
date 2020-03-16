
#Python Mini Challenge
#Fibonacci Sequence
import math
import numpy as np

def check_fib(num):
    num_sqr_plus=np.sqrt((5*num*num) + 4)
    num_sqr_minus=np.sqrt((5*num*num) - 4)
    return (num_sqr_plus - math.floor(num_sqr_plus)==0)|(num_sqr_minus - math.floor(num_sqr_minus)==0)
        
    

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 12:57:25 2021

@author: richi
"""

import argparse

def fib(n):
    if n < 0:
        fib_val = 'please try again with an integer greater than or equal to zero' 
    elif n == 0:        
        fib_val = 0    
    elif n == 1:        
        fib_val = 1    
    else:
        fib_val = fib(n - 1) + fib(n - 2)
        
    return fib_val


def main():
    parser = argparse.ArgumentParser(description='caluclate the nth number of the fibonacci sequence')
    parser.add_argument("--n", required=True, help='the nth number of the fibonacci sequence you would like to calculate')    
    args = parser.parse_args()
    num = args.n
    num = int(num)
    
    return fib(num)

    
if __name__ == '__main__':
    print(main())
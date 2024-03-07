import time
import math

a = int(input())
n = int(input())

miliseconds = n/1000

time.sleep(miliseconds)

print(f"Square root of {a} after {n} miliseconds is {math.sqrt(a)}")
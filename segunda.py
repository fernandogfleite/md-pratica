import time
from math import sqrt


eh_primo = lambda number: not any(number%i==0 for i in range(2, int(sqrt(number))))
start = time.time()

counter = 2

while (time.time()-start < 60):
    if (eh_primo(counter)):
        print(counter)
    
    counter += 1
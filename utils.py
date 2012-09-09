import math

########################################################################

#Generate prime numbers starting at a given value and going down
def reversePrimeGen(start):
    for num in range(start,2,-1):
        for factor in range(2,int(math.sqrt(num))+1):
            if num % factor == 0:
                break
        else:#if the for loop isn't broken out of we have a prime
            yield num

#Generate prime numbers starting at 2
def forwardPrimeGen():
    yield 2

    num = 3
    while 1:
        for factor in range(2,int(math.sqrt(num))+1):
            if num % factor == 0:
                break
        else:#if the for loop isn't broken out of we have a prime
            yield num

        num += 2#save a little time by just skipping even numbers
	
def is_prime(n):
    for y in range(int(math.sqrt(n))+1,1,-1):
        if index % y == 0:
            return False
	
    return True
				
########################################################################

def get_divisors(num):
    divisors = [1]
    for x in range(2,int(math.sqrt(num))+1):
        d,r = divmod(num,x)
        if r == 0:
            divisors.append(d)
            if not d == x:
                divisors.append(x)

    return divisors
	
########################################################################

def get_fibs(index):
    fibs = [1,1]
    for x in range(2,index):
        fibs.append(fibs[x-1]+fibs[x-2])

    return fibs

def next_fib(fibs):
    fibs.append(fibs[-1] + fibs[-2])
    return fibs
	
########################################################################
def binary2decimal(b_num):
    b_num = str(b_num)[::-1]

    factor = 1
    decimal = 0
    for digit in b_num:
        if digit == '1':
            decimal += factor

        factor *= 2

    return decimal

def decimal2binary(d_num,places):
    binary = ''

    factor = 1
    while factor * 2 <= d_num:
        factor *= 2

    while factor >= 1:
        if d_num - factor >= 0:
            binary += '1'
            d_num -= factor
        else:
            binary += '0'

        factor /= 2
        
    while len(binary) < places:
        binary = "0" + binary

    return binary
    
def binary2hex(b_num):
    return hex(int(b_num, 2))

def hex2binary(h_num):
    return bin(int(h_num, 16))

#####################################################################


















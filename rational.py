#Python Rational Number Math Engine

#very basic engine. must seperate all operators from fractions with spaces.
#can only do one operation at a time.
#I plan on improving this at some point to be able to handle much more.
def f_add(f1,f2,simp=True):
    n1 = f1[0]
    d1 = f1[1]
    
    n2 = f2[0]
    d2 = f2[1]
    
    n1,n2 = n1*d2,n2*d1
    cd = d1*d2
    
    fraction = (n1+n2,cd)
    
    if simp:
        return f_simplify(fraction)
    return fraction
    
def f_subtract(f1,f2,simp=True):
    n1 = f1[0]
    d1 = f1[1]
    
    n2 = f2[0]
    d2 = f2[1]
    
    n1,n2 = n1*d2,n2*d1
    cd = d1*d2
    
    fraction = (n1-n2,cd)
    
    if simp:
        return f_simplify(fraction)
    return fraction
    
def f_multiply(f1,f2):
    n1 = f1[0]
    d1 = f1[1]
    
    n2 = f2[0]
    d2 = f2[1]
    
    fraction = (n1*n2,d1*d2)
    
    if simp:
        return f_simplify(fraction)
    return fraction
    
def f_divide(f1,f2):
    n1 = f1[0]
    d1 = f1[1]
    
    n2 = f2[0]
    d2 = f2[1]
    
    n = n1*d2
    d = n2*d1
    
    #check for divide by zero
    if d == 0:
        raise Exception("Error: Divide by ZERO.")
    
    fraction = (n,d)
    
    if simp:
        return f_simplify(fraction)
    return fraction
    
def f_simplify(f):
    n = f[0]
    d = f[1]
    
    for factor in range(n,1,-1):
        if n % factor == 0 and d % factor == 0:
            return (n/factor,d/factor)
            
def f_print(f):
    n = f[0]
    d = f[1]
    
    print str(n) + "/" + str(d)
    
    

if __name__ == '__main__':
    while 1:
        data = raw_input("Enter Fractions: ")
        if data == 'q':
            break
        
        stack = data.split()
        f1 = stack[0].split('/')
        f1[0] = int(f1[0])
        f1[1] = int(f1[1])
        f2 = stack[2].split('/')
        f2[0] = int(f2[0])
        f2[1] = int(f2[1])
        
        if stack[1] == '+':
            f_print (f_add(f1,f2))
        elif stack[1] == '-':
            f_print (f_subtract(f1,f2))
        elif stack[1] == '*':
            f_print (f_multiply(f1,f2))
        elif stack[1] == '/':
            f_print (f_divide(f1,f2))
            
        
        
        
        
        
        
        
        
        
        
        
        
        
    

#RPN CALCULATOR

ops = ['+','-','*','/','%','^','sin','cos','tan','asin','acos','atan']

#Print Info
print "---------RPN Calculator---------"
print "--------Written in Python--------"
print "---------------------------------"
print "###Seperate input with spaces"
print "###Press ENTER to evaluate"
print "###('q' to quit, 'o' for valid operators)"

#Main Calculator Loop
while 1:
    print "#",
    exp = raw_input()

    #check for quit
    if exp == 'q':
        break
    if exp.strip() == '':
        continue
    if exp == 'o':
        print 'Valid Operators: +, -, *, /, %, ^, sin, cos, tan, asin, acos, atan'
        continue

    stack = []
    for item in exp.split():
        #Add numbers to the stack
        try:
            stack.append(float(item))
        except:
            if not item in ops or len(stack) < 2:
                print 'Invalid Expression Fool!!'
                break

        #Operators
        if item == '+':
            stack.append(stack.pop() + stack.pop())
        elif item == "-":
            temp = stack.pop()
            stack.append(stack.pop() - temp)
        elif item == "*":
            stack.append(stack.pop() * stack.pop())
        elif item == "/":
            temp = stack.pop()
            stack.append(stack.pop() / temp)
        elif item == "%":
            temp = stack.pop()
            stack.append(stack.pop() % temp)
        elif item == "^":
            temp = stack.pop()
            stack.append(stack.pop() ** temp)
        elif item == "sin":
            stack.append(math.sin(stack.pop()))
        elif item == "cos":
            stack.append(math.cos(stack.pop()))
        elif item == "tan":
            stack.append(math.tan(stack.pop()))
        elif item == "asin":
            stack.append(math.asin(stack.pop()))
        elif item == "acos":
            stack.append(math.acos(stack.pop()))
        elif item == "atan":
            stack.append(math.atan(stack.pop()))
    else:
        print 'Output: ' + str(stack[0])
        continue

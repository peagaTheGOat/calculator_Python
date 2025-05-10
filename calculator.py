op = input("operation: ")
n1 = ""
n2 = ""
nums = "0123456789."
operators = "+-/*"
phase = 0


for i in op:
    if phase == 0:
        if i in nums:
            n1 += i
        elif i in operators:
            sign = i
            phase = 2
    elif i in nums:
        n2 += i
        
if sign == "+":
    sign = int(n1) + int(n2)
    print(n1, "+",n2,"=", sign)
if sign == "-":
    sign = int(n1) - int(n1)
    print(n1, "-", n2,"=", sign)
    
if sign == "/":
    if n2 != "0":
        sign = int(n1) / int(n2)
        print(n1, "/",n2,"=", sign)
    else:
        print("ai nao po")
    
if sign == "*":
    sign = float(n1) * float(n2)
    print(n1, "*",n2,"=", sign)
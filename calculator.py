while True:
    op = input("operation: ")
    n1 = ""
    n2 = ""
    nums = "0123456789."
    operators = "+-/*%"
    phase = 0
    sign = ""

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
        r = str(int(n1) + int(n2))
    elif sign == "-":
        r = str(int(n1) - int(n2))
    elif sign == "*":
        r = str(int(n1) * int(n2))
    elif sign == "/":
        if int(n2) == 0:
            r = "divisão por zero é mals"
        else:
            r = str(int(n1) / int(n2))
    elif sign == "%":
        r = str((int(n1) / 100) * int(n2))
    else:
        r = "nem vc sabe oq vc quer fazer"


    if r == "divisão por zero é mals" or r == "nem vc sabe oq vc quer fazer":
        print(r)

    if len(r) > len(n1) and len(r) > len(n2) and sign != "/":
        print(" "*((len(r)-len(n1))-1), n1)
        print(sign, " "*((len(r)-len(n2)-len(sign))), n2, sep='')
        print("-"*(len(r)))
        print(r)
    
    elif sign != "/":
        if len(n2) >= len(n1):
            print(" "*(len(n2)-len(n1)+1),n1 ,sep='')
            print(sign,n2,sep='')
            print("-"*(len(n2)+1))
            print(" "*(len(n1)-len(r)),r)
        else:
            print(n1)
            print(sign," "*(len(n1)-len(n2)-1),n2 ,sep='')
            print("-"*len(n1))
            print(" "*(len(n1)-len(r)),r,sep='')
        
    elif sign == "%":
            if len(r) > len(n1) and len(r) > len(n2):
                print(" " * ((len(r) - len(n1)) - 1), n1, sep='')
                print(sign, " " * ((len(r) - len(n2) - 1)), n2, sep='')
                print("-" * len(r))
                print(r)
            else:
                maior = max(len(n1), len(n2))
                print(" " * (maior - len(n1) + 1), n1, sep='')
                print(sign, " " * (maior - len(n2)), n2, sep='')
                print("-" * (maior + 1))
                print(" " * (maior - len(r) + 1), r, sep='')

    elif sign == "/":
        if len(n2) >= len(r):
            print(n1,"|",n2,sep='')
            print("-"*(len(n1)+len(n2)+1))
            print(" "*len(n1),"|",r," "*(len(n2)-len(r)),sep='')
        else:
            print(n1,"|"," "*(len(r)-len(n2)),n2,sep='')
            print("-"*(len(n1)+len(r)+1))
            print(" "*len(n1),"|",r,sep='')

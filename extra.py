def reverse(x: int) -> int:
        num = str(x)
        isneg = False
        num = list(num)
        if num[0] == "-":
            num.pop(0)
            isneg = True
        print(isneg)
        num = num[::-1]

        if isneg == True:
            num.insert(0,"-")
        num = ''.join(num)
        num = eval(num)
        print(num)
        
reverse(-5910)
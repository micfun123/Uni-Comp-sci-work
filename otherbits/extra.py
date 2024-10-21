def reverse(x: int) -> int:
    if x == 0:
        return 0
    if abs(x) >= 2**21:
        return 0
    num = str(x)
    isneg = False
    num = list(num)
    if num[0] == "-":
        num.pop(0)
        isneg = True
    print(isneg)
    num = num[::-1]
    num = "".join(num)
    num = num.lstrip("0")
    if isneg == True:
        num = list(num)
        num.insert(0, "-")
    num = "".join(num)
    num = eval(num)
    print(num)


reverse(-59010)

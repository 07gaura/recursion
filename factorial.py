def factorial( xn):
    if (xn == 1):
        return 1;
    xnm1 = factorial(xn-1)
    print(xn)
    sum = xn * xnm1
    return sum

def main():
    xn = 3
    print(factorial(xn))
if __name__ == "__main__":
    main()

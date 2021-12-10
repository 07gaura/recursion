def power(n, xn):
    if (xn == 0):
        return 1;
    xnm1 = power(n,xn-1)
    sum = n * xnm1
    return sum

def main():
    n = 3
    xn = 3
    print(power(n, xn))
if __name__ == "__main__":
    main()

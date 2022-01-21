def main():
    n = 68
    no = None
    print(happyNum(n,no))
    
def happyNum(n,no):
    if(n==0):
        return 0
    no = n%10
    n=n//10
    sums = happyNum(n,no)
    sums = no*no + sums
    return sums
if __name__ == '__main__':
    main()

def main():
    n = 10000
    temp = n
    no = None
    sets = set()
    while True:
        
        temp = happyNum(temp,no)
        try:
            sets.remove(temp)
            return False
        except:
            sets.add(temp)
        if temp==1:
            return True
        
    
def happyNum(n,no):
    if(n==0):
        return 0
    no = n%10
    n=n//10
    sums = happyNum(n,no)
    sums = no*no + sums
    return sums
if __name__ == '__main__':
    print(main())

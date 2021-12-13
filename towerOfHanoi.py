def main():
    n = 3
    a = 10
    b = 11
    c = 12
    toh(n, a,b,c)
    
def toh(n, a, b, c):
    if n == 0:
        return
    toh(n-1, a, c,b)
    print(n,f"{a} --> {b}")
    toh(n-1,c ,b,a)
if __name__ == "__main__":
    main()

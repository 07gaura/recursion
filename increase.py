def increase(no):
    if(no == 0):
        return
    increase(no-1)
    print(no)
    
def main():
    no = 5
    increase(no)
    
if __name__ == "__main__":
    main()

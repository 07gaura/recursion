def DecreasingIncreasing(no):
    if(no == 0):
        return
    print(f'Decreasing no -> {no}')
    increase(no-1)
    print(f'Increasing no -> {no}')
    
def main():
    no = 5
    DecreasingIncreasing(no)
    
if __name__ == "__main__":
    main()

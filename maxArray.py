def main():
    arr = [1,30,20,40,3]
    idx = 0
    print(maxArray(arr, idx))
def maxArray(arr, idx):
    if(idx==len(arr)-1):
        return arr[idx]
    min = maxArray(arr, idx+1)
    if(min>arr[idx]):
        return min
    else:
        return arr[idx]
    
if __name__ == "__main__":
    main()

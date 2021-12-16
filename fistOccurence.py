def main():
    arr = [2,3,2,4,5]
    idx = 0
    n = 2
    print(fistOccurence(arr, idx, n))
    
def fistOccurence(arr, idx, data):
    if(idx == len(arr)):
        return -1
    if arr[idx]== data:
        return idx
    else:
        fo = fistOccurence(arr, idx+1,data)
        return fo
    
if __name__ == "__main__":
    main()

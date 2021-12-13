def main():
    arr = [10,20,30,40,50]
    idx = 0
    reverseArray(arr, idx)
    
def reverseArray(arr, idx):
    if idx ==  len(arr):
        return 
    reverseArray(arr,idx+1)
    print(arr[idx])
if __name__ == "__main__":
    main()

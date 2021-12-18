def main():
    arr = [2,2,3,5,4,2]
    idx = 0
    data = 2
    print(lastIndices(arr, idx, data))
def lastIndices(arr, idx, data):
    if idx == len(arr):
        return -1
    a = lastIndices(arr, idx+1, data)
    if a == -1:
        if arr[idx] == data:
            return idx
        else:
            return -1
    else:
        return a
    
if __name__ == '__main__':
    main()

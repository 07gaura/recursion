def main():
    arr = [2,2,3,5,4,2]
    idx = 0
    fsf = 0
    data = 2
    print(allIndices(arr, idx, fsf, data))
def allIndices(arr, idx, fsf, data):
    if idx == len(arr):
        return [None] * fsf
    if(data == arr[idx]):
        li1 = allIndices(arr, idx+1, fsf+1, data)
        li1[fsf] = idx
        return li1
    else:
        li1 = allIndices(arr, idx+1, fsf, data)
        return li1
        
    
if __name__ == '__main__':
    main()

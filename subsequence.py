def main():
    strr = 'abc'
    print(subsequence(strr))
    
def subsequence(strr):
    if len(strr) == 0:
        li = []
        li.append(" ")
        return li
        
    c=strr[0]
    b = strr[1:]
    sub = subsequence(b)
    li2 = []
    for i in sub:
        li2.append(i)
        li2.append(c+i)
    return li2
if __name__ == '__main__':
    main()

keypad = [".,","abc","def","ghi","jkl","mno","pqrs","tu","vwx","yz"]
def main():
    strr = "678"
    print(keypadComb(strr))

def keypadComb(strr):
    if len(strr) == 0:
        li = []
        li.append("")
        return li
    c = strr[0]
    b = strr[1:]
    
    sub  = keypadComb(b)
    
    li2 = []
    no = int(c)
    btn = keypad[no]
    
    for i in range(0,len(btn)):
        for s in sub:
            li2.append(btn[i]+s)
    return li2
    
if __name__ =="__main__":
    main()

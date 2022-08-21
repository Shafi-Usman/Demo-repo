def swap_case(s):
    # s.swapcase() easy 
    li = []
    for i in s:
        if i.islower():
           i = i.upper()
        elif i.isupper():
           i = i.lower()
        li.append(i)
    return "".join(li)
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
arr = map(int, input().split())
arr_s = list(set(arr))
big = -100
sbig = -100
for i in arr_s:
    if i > big:
        print(i)
        temp = big
        big = i
        print(str(big)+"of"+str(i))
        sbig = temp
        print(str(sbig)+"of"+str(i))
    elif i < big and i > sbig:
        print(str(sbig)+"of"+str(i)+"seco")
        sbig = i
print(sbig)
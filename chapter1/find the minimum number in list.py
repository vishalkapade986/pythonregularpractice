numberlist=[11,33,44,66,88,456]
min=numberlist[0]
for num in numberlist:
    if min>num:
        min=num
print(min)
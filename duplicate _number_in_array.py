def duplicate(numbers):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]==numbers[j]:
                print(numbers[i],"is duplicate")
                break
numbers=[1,5,5,8,7,7,9]
print(duplicate(numbers))

vowel=['a','e','i','o','u']
word="india is best country in word "
count=0
for charcter in word:
    if charcter not in vowel:
        count+=1
print(count)
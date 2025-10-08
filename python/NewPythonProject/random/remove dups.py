numbers = [1,1,2,2,4,5,77,77,8,9,9,1,2,3,4,5,6,6]
dupe=[]
for number in numbers:
    if number not in dupe:
        dupe.append(number)
dupe.sort()
print(dupe)
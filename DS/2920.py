arr = list(map(int, input().split(' ')))

ascending = True
descending = True

for i in range(1, 8): # out of range 주의!
    if (arr[i-1]<arr[i]):
        descending = False
    else:
        ascending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed") 
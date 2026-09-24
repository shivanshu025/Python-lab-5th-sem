# write a python program to count how many times a particular element appears in a list
ls=list(map(int,input("enter numbers: ").split()))
freq={}
for i in ls:
    freq[i]=freq.get(i,0)+1
print(freq)
# numbers=[10,20,30,40,50]
# search=int(input("enter number to count: "))
# count=0
# for num in numbers:
#     if num==search:
#         count=count+1
# print(count)
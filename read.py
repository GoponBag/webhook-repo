
f = open('arr2D.text','r')
count = 0
while(f.readline()):
    count = count + 1
print(count)
f.close()
f = open('arr2D.text','r')
arr=[]
for i in range (count):
    a=f.readline()
    subarr=[]
    if i == 0:
        n = a
    else:
        subarr = list(a.split(" "))
        arr.append(subarr)
print(arr)

# //////////////////////

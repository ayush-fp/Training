def count_occurrences(arr):

    v = [False for i in range(101)]
    c = [0 for i in range(101)]
    
    for j in arr:
        val = j

        if(v[val]==False):
            c[val] = 1
            v[val] = True
        
        else:
            c[val] = c[val] + 1

    for k in range(101):
        if(c[k] != 0):
            print(k,": ",c[k])

n = int(input("Enter no. of elements: "))
arr = []

for i in range(n):
    arr.append(int(input()))
      
count_occurrences(arr)
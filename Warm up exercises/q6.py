def Most_frequent(arr):

    v = [False for i in range(101)]
    c = [0 for i in range(101)]
    
    for j in arr:
        val = j

        if(v[val]==False):
            c[val] = 1
            v[val] = True
        
        else:
            c[val] = c[val] + 1

    max_index = 0
    for k in range(101):
        if(c[max_index] < c[k]):
            max_index = k
    
    return max_index

n = int(input("Enter no. of elements: "))
arr = []

for i in range(n):
    arr.append(int(input()))
      
print("\nMost frequent: ", Most_frequent(arr))
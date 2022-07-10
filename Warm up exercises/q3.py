def max_secondMax(arr):
    max_index = 0
    secondMax_index = 0
    max_val = 0
    secondMax_val = 0
    
    for i in range(len(arr)):
        if(arr[max_index] < arr[i]):
            max_index = i
    
    max_val = arr[max_index]
    secondMax_val = max_val

    arr2 = []
    for j in range(len(arr)):
        if(max_val == arr[j]):
            continue
        else:
            arr2.append(arr[j])

    #print(arr2)
    if(len(arr2) != 0):
        for k in range(len(arr2)):
            if(arr2[secondMax_index] < arr2[k]):
                secondMax_index = k
        secondMax_val = arr2[secondMax_index]
        print(secondMax_val)
    
    print("Max: ", max_val)
    print("Second Max: ", secondMax_val)

n = int(input("Enter no. of elements: "))
arr = []

for i in range(n):
    arr.append(int(input()))

max_secondMax(arr)
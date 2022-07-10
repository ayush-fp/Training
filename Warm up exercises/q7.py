def common(arr1, arr2):
    arr3 = []
    len_1 = len(arr1)
    len_2 = len(arr2)
    min_len = min(len_1, len_2)
    arr_common = []
    i = 0;
    j = 0;
    p = 0;
    q = 0;
    if(min_len == len_1):
        while(i < len_1):
            if(arr1[i] == arr2[j]):
                arr_common.append(arr1[i])
                i = i + 1
                j = j + 1
            elif(arr2[j] > arr1[i]):
                i = i + 1
            else:
                j = j + 1
    else:
        while(p < len_2):
            if(arr2[p] == arr1[q]):
                arr_common.append(arr2[p])
                p = p + 1
                continue
            if(arr1[q] > arr2[p]):
                p = p + 1
                continue
            else:
                q = q + 1
    
    return arr_common

n_1 = int(input("Enter no. of elements of arr1: "))
arr1 = []

for i in range(n_1):
    arr1.append(int(input()))

n_2 = int(input("Enter no. of elements of arr2: "))
arr2 = []

for i in range(n_2):
    arr2.append(int(input()))
print("arr1: ", arr1)
print("arr2: ", arr2)
print("Common array: ", common(arr1, arr2))
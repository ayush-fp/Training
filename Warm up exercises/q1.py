def reverse (a):
    a = a[::-1]
    return a

# def reverse2 (a):
#     b = 0
#     e = len(a) - 1
#     while(e>0):
#         temp = a[b]
#         a[b] = a[e]
#         a[e] = temp
#         b = b + 1
#         e = e - 1
#     return a

n = int(input("Enter no. of characters: "))
a = []
for i in range(n):
    a.append(input("Enter character:"))

print(a)
print(reverse(a))
#print(reverse2(a))
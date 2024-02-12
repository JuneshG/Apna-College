
# def insertionSort(arr):
#     j = 0
#     while j <= 5:
#         i = 1
#         while i <= 4:
#         # for i in range(1,len(arr)-1):
#             if arr[i] < arr[i-1]:
#                 arr[i],arr[i-1] = arr[i-1], arr[i]
#             i += 1

        
#         j +=1
#     return arr

# arr = [12,45,23,51,19,8]
# x = insertionSort(arr)
# print(x)
    
# def insertionSort(arr):
#     for j in range(1, len(arr)):
#         i = j
#         while i > 0 and arr[i] < arr[i - 1]:
#             arr[i], arr[i - 1] = arr[i - 1], arr[i]
#             i -= 1
#     return arr


# arr = [1,0]
# x = insertionSort(arr)
# print(x)



def insertionSort(arr):
    for j in range(1,len(arr)):
        i = j
        while (i > 0 and arr[i] < arr[i-1]):
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
    
    return arr

arr = [0,1,2,3,4,98,45,21,0,34,12,54,23,68,43,27,46,25,57,234,132,67,324,123,36578,1243,56,1233,41243,12,456,213,26,324,26,454,100]
x = insertionSort(arr)
print(x)



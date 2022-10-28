def buscaBinaria(arr, target):
    begin, end = 0, len(arr) - 1
    while begin < end:
        mid = (begin + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            begin = mid 
        else:
            end = mid 
    return -1


numbers = [int(x) for x in input("Введите последовательность чисел : ").split()]
sequence = list(numbers) 

for i in range (len(sequence)):
    for j in range (len(sequence)-i-1):
        if sequence[j] > sequence[j+1]:
            sequence[j], sequence[j+1] = sequence[j+1], sequence[j]


print(sequence)

def binary_search(array, element, left, right):
    if left > right:
        return False
    
    middle = (right+left) // 2 
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array,element,left,middle-1)
    else:
        return binary_search(array, element,middle+1,right)

element = int(input('Введите любое число:'))
if element < 0 or  element > 1000:
    print('Число не входит в диапазон')
    
array = [i for i in range(1,1001)]

print(binary_search(array,element,0,1000))







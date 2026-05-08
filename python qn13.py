def find_second_largest_unique(numbers):
    if len(numbers) < 2:
        return None 

    largest = float('-inf')
    secondLargest = float('-inf')

    for num in numbers:
        if num > largest:
            secondLargest = largest
            largest = num
        elif num < largest and num > secondLargest:
            secondLargest = num

    
    if secondLargest == float('-inf'):
        return None
    return secondLargest


result = find_second_largest_unique([5, 3, 9, 9, 8, 5])
print(result) 

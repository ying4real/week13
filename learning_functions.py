def findMaxInList(numbers):
    if not numbers:
        return None
    
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

print(findMaxInList([3, 7, 2, 9, 5]))
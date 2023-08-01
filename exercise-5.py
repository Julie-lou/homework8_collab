def reverse_ascending(numbers):
    for x in range(1,len(numbers)): 
        if numbers[x] <= numbers[x-1]:
            return numbers[:x][::-1]+reverse_ascending(numbers[x:])
    return numbers[::-1]

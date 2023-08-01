def reverse_ascending(numbers):
    for i in range(1,len(items)): 
        if items[i] <= items[i-1]:
            return items[:i][::-1]+reverse_ascending(items[i:])
    return items[::-1]

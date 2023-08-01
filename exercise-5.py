def reverse_ascending(numbers):
    for x in range(1,len(items)): 
        if items[x] <= items[x-1]:
            return items[:x][::-1]+reverse_ascending(items[x:])
    return items[::-1]

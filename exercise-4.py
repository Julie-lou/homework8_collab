def chunking_by(numbers, chunk):
    if len(numbers) == 0:
        return list
    new = []
    n = 1
    for i in range((len(numbers) // chunk) + 1):
        
        new.append(numbers[chunk*(n-1):chunk*n])
        n += 1
    return new
    ...

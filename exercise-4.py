def chunking_by(numbers, chunk):
    
    for i in range(chunk):
        new = []
        new.append(numbers[0:chunk])
        new.append(numbers[chunk:chunk*2])
        new.append(numbers[chunk*2:chunk*3])
        
    return new
    ...

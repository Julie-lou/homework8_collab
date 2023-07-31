def replace_last(numbers):
    if len(numbers)<=1:
        return numbers
    else:
        temp=numbers[0]
        numbers[0]=numbers[-1]
        numbers[-1]=temp
        return numbers
        
    
    

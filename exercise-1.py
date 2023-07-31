numbers=[1,2,3,4]
def replace_last(numbers):
    if len(numbers)<=1:
        return numbers
    else:
        temp=numbers[0]
        numbers[0]=numbers[-1]
        numbers[-1]=temp
        return numbers
        
    
    

def remove_all_after(numbers, n):
      list=[]
    if n in numbers:
        for number in numbers:
            if number!=n:
                list.append(number)
            elif number==n:
                list.append(number)
                break
        return list
    elif n not in numbers:
        return numbers  

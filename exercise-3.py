def remove_all_after(numbers, n):
    for x in numbers:
        new_list = []
        if n in range(len(numbers)):
            y = numbers[0:n:]
            if numbers.count(n) > 1:
                first_n = numbers.index(n)
                second_n = numbers.index(n, + first_n +1)
                y = numbers[0:second_n:]
                
            new_list.append(y)
        return new_list





def remove_all_after(numbers, n):
    new = []
    if n in numbers:
        for x in numbers:
            if x != n:
                new.append(x)
            elif x == n:
                new.append(x)
                break
        return new
    elif n not in numbers:
        return numbers
    ...

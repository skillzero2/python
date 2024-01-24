#sequence = sequence + [next_element]
#- создается копия sequence, а метод append меняет текущее состояние. 
def continue_fibonacci_sequence(sequence, n): 
    for i in range(n): 
        next_element = sequence[-1] + sequence[-2] 
        sequence.append(next_element);

sequence = [1, 1, 2, 3, 5]
continue_fibonacci_sequence(sequence, 0)
print(*sequence)

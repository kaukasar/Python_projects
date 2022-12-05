with open('input.txt', 'r') as f:
    counter = 0
    for line in f:
        if line[0] == 'A' and line[2] == 'X':
            counter += 3
        if line[0] == 'A' and line[2] == 'Y':
            counter += 4
        if line[0] == 'A' and line[2] == 'Z':
            counter += 8
        if line[0] == 'B' and line[2] == 'X':
            counter += 1
        if line[0] == 'B' and line[2] == 'Y':
            counter += 5
        if line[0] == 'B' and line[2] == 'Z':
            counter += 9
        if line[0] == 'C' and line[2] == 'X':
            counter += 2
        if line[0] == 'C' and line[2] == 'Y':
            counter += 6
        if line[0] == 'C' and line[2] == 'Z':
            counter += 7
    print(f'Totala poängen är: {counter}')
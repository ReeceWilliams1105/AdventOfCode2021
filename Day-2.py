file1 = open('day-2-input', 'r')
Lines = file1.readlines()

horizontal = 0
depth = 0
aim = 0

for line in Lines:
    instruction = line.split()
    instruction[1] = int(instruction[1])
    match instruction[0]:
        case 'forward':
            horizontal = horizontal + instruction[1]
        case 'down':
            depth = depth + instruction[1]
        case 'up':
            depth = depth - instruction[1]

print(depth*horizontal)

horizontal = 0
depth = 0

for line in Lines:
    instruction = line.split()
    instruction[1] = int(instruction[1])
    match instruction[0]:
        case 'forward':
            horizontal = horizontal + instruction[1]
            depth += aim*instruction[1]
        case 'down':
            aim += instruction[1]
        case 'up':
            aim -= instruction[1]

print(depth*horizontal)
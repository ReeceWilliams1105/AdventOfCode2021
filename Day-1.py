file1 = open('Day-1-input', 'r')
Lines = file1.readlines()

total2 = 0
total1 = 0
length = len(Lines)

prev = int(Lines[0])

for num in Lines:
    num = int(num)
    if num > prev:
        total1+=1
    prev = num

for i in range(3, length):
    group1 = int(Lines[i-2]) + int(Lines[i-1]) + int(Lines[i])
    group2 = int(Lines[i-3]) + int(Lines[i-2]) + int(Lines[i-1])
    if group1 > group2:
        total2+=1

print(total1)
print(total2)

#python loop
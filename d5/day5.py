def part_1():
    f = open("input.txt", "r")
    stacks = [[], [], [], [], [], [], [], [], []]
    lines = f.readlines()
    iter = 0
    line = lines[iter]
    while line != "\n":
        print(str(iter))
        line = lines[iter]
        n = 4
        cols = [line[i:i+n] for i in range(0, len(line), n)]
        for i in range(len(cols)):
            if "[" in cols[i]:
                stacks[i].insert(0, cols[i][1])
        iter += 1
        line = lines[iter]

    for line in lines:
        print(line)
        if "move" not in line:
            continue

        command = line.split(' ')
        command = [int(command[1]), int(command[3]), int(command[5])]

        i = 0
        while i < command[0]:
            if len(stacks[command[1]-1]) > 0:
                stacks[command[2]-1].append(stacks[command[1]-1].pop())
            i += 1
            # else:
                # print("popping from empty, bug?")

    for stack in stacks:
        print(stack[len(stack)-1], end="")

def part_2():
    f = open("input.txt", "r")
    stacks = [[], [], [], [], [], [], [], [], []]
    lines = f.readlines()
    iter = 0
    line = lines[iter]
    while line != "\n":
        print(str(iter))
        line = lines[iter]
        n = 4
        cols = [line[i:i+n] for i in range(0, len(line), n)]
        for i in range(len(cols)):
            if "[" in cols[i]:
                stacks[i].insert(0, cols[i][1])
        iter += 1
        line = lines[iter]

    for line in lines:
        print(line)
        if "move" not in line:
            continue

        command = line.split(' ')
        command = [int(command[1]), int(command[3]), int(command[5])]

        i = 0
        popped = []
        while i < command[0]:
            if len(stacks[command[1]-1]) > 0:
                popped.insert(0, stacks[command[1]-1].pop())
            i += 1

        for element in popped:
            stacks[command[2]-1].append(element)

    # print result
    for stack in stacks:
        print(stack[len(stack)-1], end="")

# part_1()
part_2()
def part_1():
    f = open("input.txt", "r")

    sum = 0
    for line in f:
        elf1 = line.split(",")[0].split("-")
        elf2 = line.split(",")[1].split("-")

        elf1_1 = int(elf1[0])
        elf1_2 = int(elf1[1])

        elf2_1 = int(elf2[0])
        elf2_2 = int(elf2[1])

        if check_overlap(elf1_1, elf1_2, elf2_1, elf2_2) or check_overlap(elf2_1, elf2_2, elf1_1, elf1_2):
            sum += 1

    print(sum)

def part_2():
    f = open("input.txt", "r")

    sum = 0
    for line in f:
        elf1 = line.split(",")[0].split("-")
        elf2 = line.split(",")[1].split("-")

        elf1_1 = int(elf1[0])
        elf1_2 = int(elf1[1])

        elf2_1 = int(elf2[0])
        elf2_2 = int(elf2[1])

        if check_overlap2(elf1_1, elf1_2, elf2_1, elf2_2) or check_overlap2(elf2_1, elf2_2, elf1_1, elf1_2):
            sum += 1

    print(sum)

def check_overlap(elf1_1, elf1_2, elf2_1, elf2_2):
    # elf2 supercedes elf1
    if elf1_1 >= elf2_1 and elf1_2 <= elf2_2:
        return True
    else:
        return False

def check_overlap2(elf1_1, elf1_2, elf2_1, elf2_2):
    # elf2 supercedes elf1
    if elf1_1 <= elf2_2 and elf1_2 >= elf2_1:
        return True
    else:
        return False

# part_1()
part_2()
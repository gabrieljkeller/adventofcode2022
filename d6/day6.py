def part_1():
    f = open("input.txt", "r")

    last_four = []
    for line in f:
        for i in range(len(line)):
            c = line[i]
            if len(last_four) < 14:
                last_four.append(c)
                continue

            temp = []
            duplicate = False
            for c2 in last_four:
                if c2 in temp:
                    duplicate = True
                temp.append(c2)
            if not duplicate:
                print("FOUND IT " + str(i))
                return
            else:
                last_four.append(c)
                last_four.pop(0)
part_1()
# not 1061
# 1081? 1080?
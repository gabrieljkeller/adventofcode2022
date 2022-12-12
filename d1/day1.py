f = open("input.txt", "r")
running_sum = 0
sums = []
for line in f:
  if line == "\n":
    sums.append(running_sum)
    running_sum = 0
  else:
    running_sum += int(line)

sums.sort(reverse=True)

print(sums[0] + sums[1] + sums[2])

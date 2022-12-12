def part_1():


  f = open("input.txt", "r")
  sum = 0
  last_bags = []
  for line in f:
    compartment_size = int(len(line)/2)
    compartment_1 = line[0:compartment_size]
    compartment_2 = line[compartment_size:len(line)]
    duplicates = []

    for c in compartment_1:
      val = to_value(c)
      if c in compartment_2 and not(val in duplicates):
        duplicates.append(val)
        sum += val
    
  print(sum)

def part_2():
  f = open("input.txt", "r")
  sum = 0
  last_bags = []

  for line in f:
    last_bags.append(line)

    if len(last_bags) > 2:
      # check all these bags, then clear, then add our own bag
      common = ""
      for c in last_bags[0]:
        not_found = False
        for i in range(len(last_bags)-1):
          if not (c in last_bags[i+1]):
            not_found = True
            break
        
        if not_found:
          continue
        else:
          common = c
          break
      
      sum += to_value(common)
      last_bags.clear()
      print(common)
    
  print(sum)
    


def to_value(c):
  return ord(c) - 96 if ord(c) > 96 else ord(c) - 38
    

part_2()
    
    
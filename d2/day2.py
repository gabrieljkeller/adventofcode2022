def part_1():
  f = open("input.txt", "r")
  points = 0
  for line in f:
    opponent = line[0]
    me = line[2]

    # 1 is rock, 2 is paper, 3 is scissors
    opponent = 1 if opponent == "A" else 2 if opponent == "B" else 3 
    me = 1 if me == "X" else 2 if me == "Y" else 3

    points += me
    if opponent == me:
      points += 3 
    if opponent == 1:
      if me == 2:
        points += 6
      elif me == 3:
        points += 0
    if opponent == 2:
      if me == 1:
        points += 0
      elif me == 3:
        points += 6
    if opponent == 3:
      if me == 1:
        points += 6
      elif me == 2:
        points += 0

  print(points)

def part_2():
  f = open("input.txt", "r")
  points = 0
  for line in f:
    opponent = line[0]
    outcome = line[2]

    # 1 is rock, 2 is paper, 3 is scissors
    opponent = 1 if opponent == "A" else 2 if opponent == "B" else 3 
    # 0 (X) is lose, 3 (Y) is end in draw, 6 (Z) is win
    outcome = 0 if outcome == "X" else 3 if outcome == "Y" else 6

    points += outcome
    if outcome == 0:
      if opponent == 1:
        points += 3 # scissors
      if opponent == 2:
        points += 1 # rock
      if opponent == 3:
        points += 2 # paper
    if outcome == 3:
      points += opponent
    if outcome == 6:
      if opponent == 1:
        points += 2 # paper
      if opponent == 2:
        points += 3 # scissors
      if opponent == 3:
        points += 1 # rock


  print(points)

part_2()
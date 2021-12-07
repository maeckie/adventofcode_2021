with open("/Users/marcus.dahlstein/Documents/git/adventofcode_2021/day_7/input.txt") as f:
    crabs = list(map(int, f.readline().split(",")))

def part1():
  all_dist = []
  for i in range(len(crabs)):
    all_dist.append(sum(list(map(lambda x: abs(x-i), crabs))))

  print(min(all_dist))

def part2():
  all_dist = []
  for i in range(len(crabs)):
    all_dist.append(sum(list(map(lambda x: abs(x-i) * (abs(x-i)+1) // 2, crabs))))
  print(min(all_dist))

part1()
part2()
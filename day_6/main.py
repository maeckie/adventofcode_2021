from collections import Counter
fish = None
with open('/Users/marcus.dahlstein/Documents/git/adventofcode_2021/day_6/input_test.txt') as f:
  fish = [line.strip().split(',') for line in f.readlines()][0]
  fish = list(map(lambda x: int(x), fish))

def part1():
  i = 0
  while i < 80:
    app = 0
    for f in range(len(fish)):
      fish[f] -= 1
      if fish[f] < 0:
        app +=1
        fish[f] = 6
    for j in range(app):
      fish.append(8)
    i+=1

  print(len(fish))



def get_cnt(days, val):
  fish = []
  fish.append(val)
  i = 0
  while i < days:
    print(fish)
    if i % 5 == 4:
      print(fish)
      exit()
    app = 0
    for f in range(len(fish)):
      fish[f] -= 1
      if fish[f] < 0:
        app +=1
        fish[f] = 6
    for j in range(app):
      fish.append(8)
    i+=1
  return len(fish)
  

def part2():
  with open("/Users/marcus.dahlstein/Documents/git/adventofcode_2021/day_6/input.txt") as f:
    fish = Counter(map(int, f.readline().split(",")))
  days = 256
  for _ in range(days):
    mamas = fish[0]
    for i in range(max(fish.keys())+1):
      fish[i] = fish.get(i + 1, 0)
    fish[6] += mamas
    fish[8] += mamas
  print(sum(fish.values()))


  
  
  
    



part2()
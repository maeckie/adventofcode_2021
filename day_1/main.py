from os import wait
import more_itertools

inp = []
with open('/Users/marcus.dahlstein/Documents/git/adventofcode/2021/day_1/input.txt') as f:
  for line in f.readlines():
    inp.append(int(line.strip()))

def part1():
  res = [x for i,x in enumerate(inp) if x > inp[i-1]]
  print(len(res))

def part2():
  w = list(map(lambda x: sum(x), list(more_itertools.windowed(inp,n=3, step=1))))
  res = [x for i,x in enumerate(w) if x > w[i-1]]
  print(len(res))

part2()
#part1()
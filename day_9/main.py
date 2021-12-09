
from functools import reduce
matrix = []
with open("/Users/marcus.dahlstein/Documents/git/adventofcode_2021/day_9/input.txt") as f:
  for line in f.readlines():
    matrix.append(list(map(lambda x: int(x), list(line.strip()))))

def part1():
  points = find_lowpoints()
  print(f"Sum part 1: {sum(points) + len(points)}")

def find_lowpoints():
  points = []
  for y in range(len(matrix)):
    for x in range(len(matrix[y])):
      y1 = matrix[y-1][x] if y-1 >= 0 else 9999
      y2 = matrix[y+1][x] if y+1 < len(matrix) else 9999
      x1 = matrix[y][x-1] if x-1 >= 0 else 9999
      x2 = matrix[y][x+1] if x+1 < len(matrix[y]) else 9999

      if matrix[y][x] < y1 and matrix[y][x] < y2 and matrix[y][x] < x1 and matrix[y][x] < x2:
          points.append((y,x))
  return points

def get_hole_size(point):
  x = point[1]
  y = point[0]
  v = 1
  matrix[y][x] = 9
  if y-1 >= 0 and matrix[y-1][x] != 9:
    v += get_hole_size((y-1,x))
  if y+1 < len(matrix) and matrix[y+1][x] != 9:
    v += get_hole_size((y+1,x))
  if x-1 >= 0 and matrix[y][x-1] != 9:
    v += get_hole_size((y,x-1))
  if x+1 < len(matrix[0]) and matrix[y][x+1] != 9:
    v += get_hole_size((y,x+1))
  return v

def part2():
  all_things = []
  points = find_lowpoints()
  for p in points:
    all_things.append(get_hole_size(p))
  all_things = sorted(all_things)
  s = reduce((lambda x, y: x * y), all_things[-3:])
  print(s)
part1()
part2()
import re, time


def calc_line(x1,y1,x2,y2):
  deltax = abs(x1-x2)
  deltay = abs(y1-y2)
  line = []
  if deltax == 0:
    mi = y1 if y1 < y2 else y2
    ma = y2 if y2 > y1 else y1
    line = [(x1,y) for y in range(mi,ma+1)]
  elif deltay == 0:
    mi = x1 if x1 < x2 else x2
    ma = x2 if x2 > x1 else x1
    line = [(x,y1) for x in range(mi,ma+1)]
  else:
    mi = x1 if x1 < x2 else x2
    ma = x2 if x2 > x1 else x1
    ymi = y1 if y1 < y2 else y2
    q = 0
    for i in range(mi,ma+1):
      line.append((i,ymi+q))
      q+=1
  return line


def main(part="part1"):
  coord = {}
  with open('/Users/marcus.dahlstein/Documents/git/adventofcode_2021/day_5/input.txt') as f:
    for line in f.readlines():
      m = re.match(r'(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)',line.strip())
      x1 = int(m.group('x1'))
      x2 = int(m.group('x2'))
      y1 = int(m.group('y1'))
      y2 = int(m.group('y2'))
      if part == "part1" and not (x1 == x2 or y1 == y2):
        continue
      coordinates = calc_line(x1,y1,x2,y2)
      for x,y in coordinates:
        pos = f"{x},{y}"
        if pos not in coord:
          coord[pos] = 0
        coord[pos] += 1
      




  overlaps = 0
  for k in coord:
    if coord[k] > 1:
      overlaps += 1
  print(f"{part} has overlaps in {overlaps} places")

      

start_time = time.time()
main()     
main("part2")
print("--- %s seconds ---" % (time.time() - start_time))


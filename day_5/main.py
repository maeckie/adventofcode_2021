import re, pprint



def get_range(a,b):
  if a < b:
    return range(a,b+1)
  return range(b,a+1)

def q(x0, y0, x1, y1):
    deltax = x1-x0
    dxsign = int(abs(deltax)/deltax)
    deltay = y1-y0
    dysign = int(abs(deltay)/deltay)
    deltaerr = abs(deltay/deltax)
    error = 0
    y = y0
    for x in range(x0, x1, dxsign):
        yield x, y
        error = error + deltaerr
        while error >= 0.5:
            y += dysign
            error -= 1
    yield x1, y1
def main(part="part1"):
  coord = {}
  with open('/Users/marcus.dahlstein/Documents/git/adventofcode_2021/day_5/input.txt') as f:
    for line in f.readlines():
      m = re.match(r'(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)',line.strip())
      x1 = int(m.group('x1'))
      x2 = int(m.group('x2'))
      y1 = int(m.group('y1'))
      y2 = int(m.group('y2'))
      
      if x1 == x2:
        for i in get_range(y1,y2):
          pos = f"{x1},{i}"
          if pos not in coord:
            coord[pos] = 0
          coord[pos] += 1
      elif y1 == y2:
        for i in get_range(x1,x2):
          pos = f"{i},{y1}"
          if pos not in coord:
            coord[pos] = 0
          coord[pos] += 1
      else:
        if part == "part1":
          continue
        #print(f"x1: {x1}, x1: {x2}, y1: {y1}, y2: {y2}")
        coordinates =q(x1,y1,x2,y2)
        for x,y in list(coordinates):
          pos = f"{x},{y}"
          if pos not in coord:
            coord[pos] = 0
          coord[pos] += 1
      




  overlaps = 0
  for k in coord:
    if coord[k] > 1:
      overlaps += 1
  #pprint.pprint(coord)
  print(f"{part} has overlaps in {overlaps} places")

      

main()     
main("part2")
import re
commands = []
with open('/Users/marcus.dahlstein/Documents/git/adventofcode_2021/day_2/input.txt') as f:
  for line in f.readlines():
    m = re.match('(\w+)\s(\d+)', line)
    commands.append((m.group(1), int(m.group(2))))

def solve(commands):
  pos = [0,0]
  aim = 0
  pos2 = [0,0]
  for command in commands:
    if command[0] == 'forward':
      pos[0] += command[1]
      pos2[0] += command[1]
      pos2[1] += aim * command[1]
    elif command[0] == 'down':
      pos[1] += command[1]
      aim += command[1]
    elif command[0] == 'up':
      pos[1] -= command[1]
      aim -= command[1]
  
  print(f"Part 1: {pos[0]*pos[1]}")
  print(f"Part 2: {pos2[0]*pos2[1]}")

solve(commands)

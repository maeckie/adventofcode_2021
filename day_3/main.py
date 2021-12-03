
import copy
report = {}
report_vanilla = []
with open('/Users/marcus.dahlstein/Documents/git/adventofcode_2021/day_3/input.txt') as f:
  for line in f.readlines():
    report_vanilla.append(line.strip())
    for i in range(len(line.strip())):
      if i not in report:
        report[i] = []
      report[i].append(line[i])



def part1():
  epsilon = ''
  gamma = ''
  for k in report:
    a = report[k].count('0')
    b = report[k].count('1')
    if a > b:
      gamma += '0'
      epsilon += '1'
    else:
      gamma += '1'
      epsilon += '0'


  print(int(gamma,2) * int(epsilon,2))

def  ox_and_co2(report_vanilla, kind):
  for i in range(len(report_vanilla[0])):
    one = 0
    zero = 0
    for v in report_vanilla:
      if v[i] == '1':
        one += 1
      else:
        zero += 1
    
    if kind == 'co2':
      look_for = '0'
      if zero > one:
        look_for = '1'
    else:
      look_for = '0'
      if one >= zero:
        look_for = '1'
    
    p = 0
    tbp = []
    for v in report_vanilla:
      if v[i] != look_for:
        tbp.append(p)
      p+=1
    for p in reversed(tbp):
      report_vanilla.pop(p)
    
    if len(report_vanilla) == 1:
      break
  
  return int(report_vanilla[0],2)
  
def part2():

  co_2 = ox_and_co2(copy.deepcopy(report_vanilla), "co2")
  ox_2 = ox_and_co2(copy.deepcopy(report_vanilla), "ox")
  print(ox_2*co_2)
      
part1()
part2()
  
 


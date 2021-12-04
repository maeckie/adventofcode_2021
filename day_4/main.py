import re, pprint
bingo_balls = []
bingo_cards = []
bingo_card = []

def get_sum(card, drawn):
  for row in card:
    for nr in range(len(row)):
      if row[nr] in drawn:
        row[nr] = 0 
  summa = 0
  for row in card:
    summa += sum(row)
  return summa
          
with open('/Users/marcus.dahlstein/Documents/git/adventofcode_2021/day_4/input.txt') as f:
  for line in f.readlines():
    if ',' in line:
      bingo_balls = list(map(lambda x: int(x),line.strip().split(',')))
      continue
    if ' ' in line:
      l = re.split(r'\s+', line.strip())
      bingo_card.append(list(map(lambda x: int(x),l)))
    else:
      if len(bingo_card) > 0:
        bingo_cards.append(bingo_card)
        bingo_card = []
  bingo_cards.append(bingo_card)
      
def part1():
  for i in range(0,len(bingo_balls)):
    for card in bingo_cards:
      for row in card:
        if isRowWin(card, bingo_balls[:i]) or isColumnWin(card, bingo_balls[:i]):
          summa = get_sum(card, bingo_balls[:i])
          last_ball = bingo_balls[i-1]
          print(last_ball * summa)
          exit()


def isRowWin(card, balls):
  for row in card:
        is_match = set(row).intersection(set(balls))
        if len(is_match) == 5:
          return True
  return False

def isColumnWin(card, balls):
  for i in range(len(card[0])):
    col = []
    for c in card:
      col.append(c[i])
    is_match = set(col).intersection(set(balls))
    if len(is_match) == 5:
          return True
  return False
  


def part2():
  winning_ticket = None
  balls = []
  all_winners = []
  for i in range(0,len(bingo_balls)):
    for card in bingo_cards:
      if isRowWin(card, bingo_balls[:i]) or isColumnWin(card, bingo_balls[:i]):
        if card not in all_winners:
          winning_ticket = (card)
          balls = bingo_balls[:i]
          all_winners.append(card)
  
  print(get_sum(winning_ticket, balls)*balls[-1])

#part1()
part2()

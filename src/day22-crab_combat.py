from santas_little_helpers import *
from collections import deque

today = day(2020, 22)


def score(deck):
  return sum((val + 1) * card for val, card in enumerate(reversed(deck)))


def combat(init_decks):
  p1 = deque(init_decks[0])
  p2 = deque(init_decks[1])

  while len(p1) > 0 and len(p2) > 0:
    p1c, p2c = p1.popleft(), p2.popleft()
    target = p1 if p1c > p2c else p2

    target.append(max(p1c, p2c))
    target.append(min(p1c, p2c))

  winner = p1 if len(p1) > len(p2) else p2
  return score(winner)


def recursive_combat(p1, p2):
  seen = set()
  while len(p1) > 0 and len(p2) > 0:
    cache_key = tuple(p1), tuple(p2)
    if cache_key in seen:
      winner = p1
      break
    seen.add(cache_key)
    p1c, p2c = p1.popleft(), p2.popleft()
    if len(p1) >= p1c and len(p2) >= p2c:
      p1d, p2d = deque(list(p1)[:p1c]), deque(list(p2)[:p2c])
      winner = p1 if next(recursive_combat(p1d, p2d)) == 1 else p2
    else:
      winner = p1 if p1c > p2c else p2
    winner.append(p1c if winner is p1 else p2c)
    winner.append(p2c if winner is p1 else p1c)

  yield 1 if winner == p1 else 2
  yield score(winner)


def parse(line):
  _, cards = line.split(':', 1)
  return deque(map(int, cards.split()))


def main():
  init_decks = list(get_data(today, [('func', parse)], groups=True))
  print(f'{today} star 1 = {combat(init_decks)}')
  score = skip(1, recursive_combat(init_decks[0], init_decks[1]))
  print(f'{today} star 2 = {score}')


if __name__ == '__main__':
  timed(main)

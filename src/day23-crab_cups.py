from santas_little_helpers import *

today = day(2020, 23)

jump = []


class Cup:
  def __init__(self, label, n_cup=None):
    self.label = label
    self.n_cup = n_cup

  def __eq__(self, value): return self.label == value
  def __ne__(self, value): return self.label != value
  def __mul__(self, other): return self.label * other.label

  def __matmul__(self, ns):
    if ns == 1:
      return self.n_cup
    target = self.n_cup
    while ns > 1:
      target = target.n_cup
      ns -= 1
    return target


def get_target(current, a, b, c, limit):
  t = current.label - 1 or limit
  while t == a or t == b or t == c:
    t = t - 1 or limit
  return jump[t]


def splice(target, chain_start, chain_end):
  original_n = target @ 1
  target.n_cup = chain_start
  chain_end.n_cup = original_n


def play_game(init_order, cup_count=10, iterations=100):
  cups = [Cup(label) for label in init_order]
  if cup_count > 10:
    cups.extend(Cup(label) for label in range(10, cup_count + 1))
  for left, right in zip(cups, cups[1:] + [cups[0]]):
    left.n_cup = right
  jump.clear()
  jump.append(None)
  for cup in sorted(cups, key=lambda c: c.label):
    jump.append(cup)

  current = cups[0]
  for _ in range(iterations):
    a = chain_start = current @ 1
    b = chain_middle = chain_start @ 1
    c = chain_end = chain_middle @ 1

    next_cup = chain_end @ 1
    current.n_cup = next_cup

    target = get_target(current, a, b, c, cup_count)
    splice(target, chain_start, chain_end)

    current = next_cup
  return jump[1]


def play_short_game(init_order):
  cup = play_game(init_order, len(init_order))
  result = ''
  while cup @ 1 != 1:
    cup @= 1
    result += str(cup.label)
  return result


def play_long_game(init_order):
  cup_one = play_game(init_order, 1_000_000, 10_000_000)
  return (cup_one @ 1) * (cup_one @ 2)


def main():
  init_order = next(get_data(today, base_ops + [('map', int)]))
  print(f'{today} star 1 = {play_short_game(init_order)}')
  print(f'{today} star 2 = {play_long_game(init_order)}')


if __name__ == '__main__':
  timed(main)

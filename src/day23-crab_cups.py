from santas_little_helpers import *

today = day(2020, 23)

jump = dict()


class Cup:
  def __init__(self, label, n_cup=None):
    self.label = label
    self.n_cup = n_cup

  def __matmul__(self, ns):
    target = self.n_cup
    while ns > 1:
      target = target.n_cup
      ns -= 1
    return target


def get_target(current, chain_pointer, limit):
  illegal = set()
  for _ in range(3):
    illegal.add(chain_pointer.label)
    chain_pointer @= 1
  target = limit if current.label == 1 else current.label - 1
  while target in illegal:
    target = limit if target == 1 else target - 1
  return jump[target]


def splice(target, chain_pointer):
  original_n = target @ 1
  target.n_cup = chain_pointer
  (chain_pointer @ 2).n_cup = original_n


def play_game(init_order, cup_count=10, iterations=100):
  cups = [Cup(label) for label in init_order]
  if cup_count > 10:
    cups.extend(Cup(label) for label in range(10, cup_count + 1))
  for left, right in zip(cups, cups[1:] + [cups[0]]):
    left.n_cup = right
  for cup in cups:
    jump[cup.label] = cup

  current = cups[0]
  for _ in range(iterations):
    chain_pointer = current @ 1
    current.n_cup = chain_pointer @ 3

    target = get_target(current, chain_pointer, cup_count)
    splice(target, chain_pointer)

    current @= 1
  return jump[1]


def play_short_game(init_order):
  cup = play_game(init_order, len(init_order))
  result = ''
  while (cup @ 1).label != 1:
    cup @= 1
    result += str(cup.label)
  return result


def play_long_game(init_order):
  cup_one = play_game(init_order, 1_000_000, 10_000_000)
  return (cup_one @ 1).label * (cup_one @ 2).label


def main():
  init_order = next(get_data(today, base_ops + [('map', int)]))
  print(f'{today} star 1 = {play_short_game(init_order)}')
  print(f'{today} star 2 = {play_long_game(init_order)}')


if __name__ == '__main__':
  timed(main)

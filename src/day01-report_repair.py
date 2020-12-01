from santas_little_helpers import day, get_data, timed
from itertools import combinations

today = day(2020, 1)


def part1(ns):
  for n1, n2 in combinations(ns, 2):
    if n1 + n2 == 2020:
      return n1 * n2


def part2(ns):
  for n1, n2, n3 in combinations(ns, 3):
    if n1 + n2 + n3 == 2020:
      return n1 * n2 * n3


def main() -> None:
  inp = list(get_data(today, [('func', int)]))
  print(f'{today} star 1 = {part1(inp)}')
  print(f'{today} star 2 = {part2(inp)}')


if __name__ == '__main__':
  timed(main)

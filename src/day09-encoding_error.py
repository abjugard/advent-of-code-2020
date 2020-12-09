from santas_little_helpers import *
from itertools import combinations

today = day(2020, 9)


def find_xmas_magic(inp):
  for i in range(25, len(inp)):
    combs = combinations(inp[i - 25:i], 2)
    if not any(sum(comb) == inp[i] for comb in combs):
      return inp[i]


def crack_xmas(magic_number, inp):
  for i in range(len(inp)):
    s = [inp[i]]
    for j in range(i + 1, len(inp)):
      s += [inp[j]]
      if sum(s) == magic_number:
        return min(s) + max(s)
      if sum(s) > magic_number:
        break


def parse(line):
  return line


def main():
  inp = list(get_data(today, base_ops + [
    ('func', int)
  ], groups=False))
  magic_number = find_xmas_magic(inp)
  print(f'{today} star 1 = {magic_number}')
  print(f'{today} star 2 = {crack_xmas(magic_number, inp)}')


if __name__ == '__main__':
  timed(main)

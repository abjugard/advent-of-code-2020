from santas_little_helpers import day, get_data, timed, base_ops
from itertools import starmap
from collections import Counter
from operator import xor

today = day(2020, 2)


def parse(pwd):
  ns, pwd = pwd.split(' ', maxsplit=1)
  n1, n2 = ns.split('-')
  return int(n1), int(n2), *pwd.split(': ')


def is_valid1(min_count, max_count, letter, pwd):
  d = Counter(pwd)
  return d[letter] >= min_count and d[letter] <= max_count


def is_valid2(n1, n2, letter, pwd):
  return xor(pwd[n1 - 1] == letter, pwd[n2 - 1] == letter)


def main() -> None:
  inp = list(get_data(today, base_ops + [('func', parse)]))
  print(f'{today} star 1 = {sum(starmap(is_valid1, inp))}')
  print(f'{today} star 2 = {sum(starmap(is_valid2, inp))}')


if __name__ == '__main__':
  timed(main)

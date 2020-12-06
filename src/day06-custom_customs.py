from santas_little_helpers import day, get_data, timed
from collections import Counter

today = day(2020, 6)


def count_any(groups):
  return sum(len(d) for d, _ in groups)


def count_common(groups):
  return sum(sum(count == n for count in d.values()) for d, n in groups)


def parse(group):
  return Counter(group.replace('\n', '')), len(group.split())


def main():
  groups = list(get_data(today, [('func', parse)], groups=True))
  print(f'{today} star 1 = {count_any(groups)}')
  print(f'{today} star 2 = {count_common(groups)}')


if __name__ == '__main__':
  timed(main)

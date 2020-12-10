from santas_little_helpers import *
from functools import lru_cache

today = day(2020, 10)

adapters = []
target = None


def joltage_differences():
  diff = [0, 0, 0]
  last = 0
  for adp in adapters:
    if last is not None:
      d = adp - last
      diff[d - 1] += 1
    last = adp
  return diff[0] * (diff[2] + 1)


def can_plug(next_joltage, current_joltage):
  return next_joltage - current_joltage <= 3


@lru_cache
def combinations(idx=0, joltage=0):
  if idx == len(adapters):
    return can_plug(target, joltage)

  total = combinations(idx + 1, joltage)
  if can_plug(adapters[idx], joltage):
    total += combinations(idx + 1, adapters[idx])
  return total


def main():
  global adapters, target
  adapters = list(sorted(get_data(today, [('func', int)])))
  target = max(adapters) + 3
  print(f'{today} star 1 = {joltage_differences()}')
  print(f'{today} star 2 = {combinations()}')


if __name__ == '__main__':
  bench(main)

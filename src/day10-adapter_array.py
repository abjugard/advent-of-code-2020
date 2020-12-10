from santas_little_helpers import *

today = day(2020, 10)

cache = {}


def joltage_differences(adapters):
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


def combinations(remaining, joltage, target):
  cache_key = (joltage, len(remaining))
  if cache_key in cache:
    return cache[cache_key]

  if len(remaining) == 0:
    return can_plug(target, joltage)
  adapter, *remaining = remaining
  total = combinations(remaining, joltage, target)
  if can_plug(adapter, joltage):
    total += combinations(remaining, adapter, target)

  cache[cache_key] = total + can_plug(target, joltage)
  return total


def main():
  adapters = list(sorted(get_data(today, [('func', int)])))
  print(f'{today} star 1 = {joltage_differences(adapters)}')
  print(f'{today} star 2 = {combinations(adapters, 0, max(adapters) + 3)}')


if __name__ == '__main__':
  bench(main)

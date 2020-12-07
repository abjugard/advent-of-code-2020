from santas_little_helpers import day, get_data, timed
import re

today = day(2020, 7)

d = None
outer_re = re.compile(r'(.+) bags contain (.+)\.')
inner_re = re.compile(r'(\d+) (.+?) bags?')


def find(target, bag):
  if target == bag:
    return True
  options = d[bag]
  if options is None:
    return False
  return any(find(target, other) for other in options.keys())


def count(bag):
  options = d[bag]
  if options is None:
    return 0
  direct = sum(options.values())
  nested = sum(amt * count(other) for other, amt in options.items())
  return direct + nested


def parse(line):
  outer, inner = outer_re.match(line).groups()

  if inner == 'no other':
    return outer, None

  bags = {color: int(count) for count, color in inner_re.findall(line)}

  return outer, bags


def main():
  global d
  d = dict(get_data(today, [('func', parse)]))
  target = 'shiny gold'
  combinations = sum(find(target, bag) for bag in d.keys() if bag != target)
  print(f'{today} star 1 = {combinations}')
  print(f'{today} star 2 = {count(target)}')


if __name__ == '__main__':
  timed(main)

from santas_little_helpers import day, get_data, timed

today = day(2020, 7)

d = None


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
  outer, inner = line.split(' bags contain ')

  inner = inner.replace('.', '').replace(' bags', '').replace(' bag', '')
  if inner == 'no other':
    return outer, None

  bags = []
  for bag in inner.split(', '):
    count, color = bag.split(' ', 1)
    bags.append((color, int(count)))

  return outer, dict(bags)


def main():
  global d
  d = dict(get_data(today, [('func', parse)]))
  target = 'shiny gold'
  combinations = sum(find(target, bag) for bag in d.keys() if bag != target)
  print(f'{today} star 1 = {combinations}')
  print(f'{today} star 2 = {count(target)}')


if __name__ == '__main__':
  timed(main)

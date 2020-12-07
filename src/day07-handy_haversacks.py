from santas_little_helpers import day, get_data, timed
from collections import defaultdict
import re

today = day(2020, 7)

outer_re = re.compile(r'(.+) bags contain (.+)\.')
inner_re = re.compile(r'(\d+) (.+?) bags?')

contents = defaultdict(dict)
contained_in = defaultdict(set)


def find(target):
  cs = set(contained_in[target])
  for c in contained_in[target]:
    cs.update(find(c))
  return cs


def contains(bag):
  return sum(n + n * contains(other) for other, n in contents[bag].items())


def setup(line):
  outer, inner = outer_re.match(line).groups()
  for count, color in inner_re.findall(line):
    contained_in[color].add(outer)
    contents[outer][color] = int(count)


def main():
  list(get_data(today, [('func', setup)]))
  print(f'{today} star 1 = {len(find("shiny gold"))}')
  print(f'{today} star 2 = {contains("shiny gold")}')


if __name__ == '__main__':
  timed(main)

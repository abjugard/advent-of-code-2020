from santas_little_helpers import *

today = day(2020, XX)


def part1(inp):
  print(inp)


def part2(inp):
  print(inp)


def parse(line):
  return line


def main():
  inp = list(get_data(today, base_ops + [
    # ('func', parse)
  ], groups=False))
  star1 = part1(inp)
  print(f'{today} star 1 = {star1}')
  # submit_answer(today, star1)
  # star2 = part2(inp)
  # print(f'{today} star 2 = {star2}')
  # submit_answer(today, star2, 2)


if __name__ == '__main__':
  timed(main)

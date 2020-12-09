from santas_little_helpers import *
from itertools import combinations

today = day(2020, 9)


def find_xmas_magic(xmas_data):
  for i in range(25, len(xmas_data)):
    preceeding_pairs = combinations(xmas_data[i - 25:i], 2)
    if all(sum(pair) != xmas_data[i] for pair in preceeding_pairs):
      return xmas_data[i]


def crack_xmas(magic_number, xmas_data):
  chunk_start = 0
  while xmas_data[chunk_start] < magic_number:
    chunk_sum = xmas_data[chunk_start]
    for chunk_end in range(chunk_start + 1, len(xmas_data)):
      next_val = xmas_data[chunk_end]
      chunk_sum += next_val
      if chunk_sum < magic_number:
        continue
      chunk = xmas_data[chunk_start:chunk_end]
      if chunk_sum == magic_number:
        return min(chunk) + max(chunk)
      if chunk_sum > magic_number:
        skip = 1
        while sum(chunk[:skip + 1]) <= next_val:
          skip += 1
        chunk_start += skip
        break


def main():
  xmas_data = list(get_data(today, [('func', int)]))
  magic_number = find_xmas_magic(xmas_data)
  print(f'{today} star 1 = {magic_number}')
  print(f'{today} star 2 = {crack_xmas(magic_number, xmas_data)}')


if __name__ == '__main__':
  timed(main)

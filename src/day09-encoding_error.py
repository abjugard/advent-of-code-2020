from santas_little_helpers import *
from collections import deque

today = day(2020, 9)


def find_xmas_magic(xmas_data):
  for idx in range(25, len(xmas_data)):
    defect = xmas_data[idx]
    preamble = set(xmas_data[idx - 25:idx])
    for other in preamble:
      if defect - other in preamble:
        break
    else:
      return defect


def crack_xmas(magic_number, xmas_data):
  chunk = deque()
  data = deque(xmas_data)
  chunk_sum = 0
  while chunk_sum != magic_number:
    next_val = data.popleft()
    chunk_sum += next_val
    chunk.append(next_val)
    while chunk_sum > magic_number:
      chunk_sum -= chunk.popleft()
  return min(chunk) + max(chunk)


def main():
  xmas_data = list(get_data(today, [('func', int)]))
  magic_number = find_xmas_magic(xmas_data)
  print(f'{today} star 1 = {magic_number}')
  print(f'{today} star 2 = {crack_xmas(magic_number, xmas_data)}')


if __name__ == '__main__':
  timed(main)

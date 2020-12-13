from santas_little_helpers import *
from sympy.ntheory.modular import crt

today = day(2020, 13)


def part1(earliest, buses):
  buses = [bus for bus in buses if bus != 'x']
  n_bus, time_to_wait = None, None
  for bus in buses:
    time = (earliest // bus) * bus
    while time < earliest:
      time += bus
    n_time = time - earliest
    if time_to_wait is None or n_time < time_to_wait:
      time_to_wait = n_time
      n_bus = bus
  return n_bus * time_to_wait


def part2(buses):
  offsets = [-offset for offset, bus in enumerate(buses) if bus != 'x']
  buses = [bus for bus in buses if bus != 'x']
  return crt(buses, offsets)[0]


def parse(inp):
  earliest = int(next(inp))
  buses = [b if b == 'x' else int(b) for b in next(inp).split(',')]
  return earliest, buses


def main():
  earliest, buses = parse(get_data(today))
  print(f'{today} star 1 = {part1(earliest, buses)}')
  print(f'{today} star 2 = {part2(buses)}')


if __name__ == '__main__':
  timed(main)

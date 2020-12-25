from santas_little_helpers import *

today = day(2020, 25)

modulo = 20201227


def determine_loop_size(public_key):
  value = 1
  loop_size = 0
  while value != public_key:
    loop_size += 1
    value *= 7
    value %= modulo
  return loop_size


def crack_door_encryption(public_keys):
  loop_size = determine_loop_size(next(public_keys))
  return pow(next(public_keys), loop_size, modulo)


def main():
  public_keys = get_data(today, [('func', int)])
  print(f'{today} star 1 = {crack_door_encryption(public_keys)}')


if __name__ == '__main__':
  timed(main)

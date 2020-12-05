from santas_little_helpers import day, get_data, timed

today = day(2020, 5)


def find_seat(seats):
  for seat in seats:
    if seat + 1 not in seats and seat + 2 in seats:
      return seat + 1


def main():
  seats = set(get_data(today, [
    ('translate', ('FBLR', '0101')),
    ('func', (int, [2]))
  ]))
  print(f'{today} star 1 = {max(seats)}')
  print(f'{today} star 2 = {find_seat(seats)}')


if __name__ == '__main__':
  timed(main)

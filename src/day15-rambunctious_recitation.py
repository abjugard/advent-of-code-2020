from santas_little_helpers import *

today = day(2020, 15)


def play_game(init_rounds, game_length):
  seen = {n: i for i, n in enumerate(init_rounds)}
  last = 0

  for turn in range(len(init_rounds), game_length - 1):
    n = turn - seen[last] if last in seen else 0
    seen[last] = turn
    last = n

  return last


def main():
  init_rounds = next(get_data(today, [('split', ','), ('map', int)]))
  print(f'{today} star 1 = {play_game(init_rounds, 2020)}')
  print(f'{today} star 2 = {play_game(init_rounds, 30000000)}')


if __name__ == '__main__':
  timed(main)

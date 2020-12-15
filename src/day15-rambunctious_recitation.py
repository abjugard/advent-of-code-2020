from santas_little_helpers import *

today = day(2020, 15)


def play_game(init_rounds, target_turns):
  seen = {n: i for i, n in enumerate(init_rounds)}
  last = 0

  for turn in range(len(init_rounds), max(target_turns)):
    n = (turn - seen[last]) if last in seen else 0

    if turn + 1 in target_turns:
      yield last

    seen[last] = turn
    last = n


def main():
  init_rounds = next(get_data(today, [('split', ','), ('map', int)]))
  star = play_game(init_rounds, [2020, 30000000])
  print(f'{today} star 1 = {next(star)}')
  print(f'{today} star 2 = {next(star)}')


if __name__ == '__main__':
  timed(main)

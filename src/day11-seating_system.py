from santas_little_helpers import *

today = day(2020, 11)

h = w = None
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def get_adjacent(grid, y, x):
  for yd, xd in dirs:
    yp, xp = y + yd, x + xd
    if 0 <= yp < h and 0 <= xp < w:
      pos = grid[yp][xp]
      if pos == '.':
        continue
      if pos == '#':
        yield True
      elif pos == 'L':
        yield False


def can_see(grid, y, x):
  for yd, xd in dirs:
    yp, xp = y + yd, x + xd
    while 0 <= yp < h and 0 <= xp < w:
      pos = grid[yp][xp]
      if pos == '.':
        yp += yd
        xp += xd
        continue
      elif pos == '#':
        yield True
      elif pos == 'L':
        yield False
      break


def iterate(grid, tolerance=4, tolerance_func=get_adjacent):
  n_grid = []
  for y in range(len(grid)):
    n_row = grid[y].copy()
    for x, current in enumerate(grid[y]):
      if current not in '#L':
        continue
      taken_seats = tolerance_func(grid, y, x)
      if current == 'L':
        if not any(taken_seats):
          n_row[x] = '#'
      elif current == '#':
        if sum(taken_seats) >= tolerance:
          n_row[x] = 'L'
    n_grid.append(n_row)
  return n_grid


def game_of_life(grid, extended_rules=False):
  tolerance = 5 if extended_rules else 4
  tolerance_func = can_see if extended_rules else get_adjacent

  prev = None
  while prev != grid:
    prev = grid
    grid = iterate(prev, tolerance, tolerance_func)
  tot = 0
  for row in grid:
    tot += sum(seat == '#' for seat in row)
  return tot


def main():
  global h, w
  start_grid = list(get_data(today, base_ops + [('func', list)]))
  h, w = len(start_grid), len(start_grid[0])
  print(f'{today} star 1 = {game_of_life(start_grid)}')
  print(f'{today} star 2 = {game_of_life(start_grid, extended_rules=True)}')


if __name__ == '__main__':
  timed(main)

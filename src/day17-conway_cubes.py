from santas_little_helpers import *
from collections import defaultdict

today = day(2020, 17)

start_h = start_w = None
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]


def get_adjacent(cube, p, hypercube):
  x, y, z, w = p
  hypercycle = range(-1, 2) if hypercube else range(1)
  for wd in hypercycle:
    for zd in range(-1, 2):
      for xd, yd in dirs:
        n_p = x + xd, y + yd, z + zd, w + wd
        if n_p == p or n_p not in cube:
          continue
        yield cube[n_p]


def iterate(cube, cycle, hypercube=False):
  cycle += 1
  n_cube = defaultdict(lambda: False)
  hypercycle = range(-cycle, 1 + cycle) if hypercube else range(1)
  for w in hypercycle:
    for z in range(-cycle, 1 + cycle):
      for y in range(-cycle, start_h + cycle):
        for x in range(-cycle, start_w + cycle):
          p = (x, y, z, w)
          active = cube[p]
          adjacent_active = sum(get_adjacent(cube, p, hypercube))
          if adjacent_active == 2 and active or adjacent_active == 3:
            n_cube[p] = True
  return n_cube


def game_of_life(cube, hypercube=False):
  for cycle in range(6):
    cube = iterate(cube, cycle, hypercube)
  return sum(cube.values())


def main():
  global start_h, start_w
  cube = defaultdict(lambda: False)
  start_grid = list(get_data(today, base_ops + [('func', list)]))
  start_h, start_w = len(start_grid), len(start_grid[0])
  for y, l in enumerate(start_grid):
    for x, p in enumerate(l):
      if p == '#':
        cube[(x, y, 0, 0)] = True
  print(f'{today} star 1 = {game_of_life(cube)}')
  print(f'{today} star 2 = {game_of_life(cube, True)}')


if __name__ == '__main__':
  timed(main)

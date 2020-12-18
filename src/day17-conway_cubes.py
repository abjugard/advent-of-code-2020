from santas_little_helpers import *
from itertools import product

today = day(2020, 17)

start_h = start_w = None

cube_offsets = list(product(*[range(-1, 2)] * 3, {0}))
hypercube_offsets = list(product(*[range(-1, 2)] * 4))


def get_adjacent(cube, p, hypercube):
  x, y, z, w = p
  offsets = hypercube_offsets if hypercube else cube_offsets
  for xd, yd, zd, wd in offsets:
    n_p = x + xd, y + yd, z + zd, w + wd
    if n_p == p or n_p not in cube:
      continue
    yield cube[n_p]


def iterate(cube, cycle, hypercube=False):
  cycle += 1
  n_cube = dict()
  w_range = range(-cycle, 1 + cycle) if hypercube else range(1)
  for w in w_range:
    for z in range(-cycle, 1 + cycle):
      for y in range(-cycle, start_h + cycle):
        for x in range(-cycle, start_w + cycle):
          p = (x, y, z, w)
          active = sum(get_adjacent(cube, p, hypercube))
          if active == 3:
            n_cube[p] = True
          elif active == 2 and cube.get(p, False):
            n_cube[p] = True
  return n_cube


def game_of_life(cube, hypercube=False):
  for cycle in range(6):
    cube = iterate(cube, cycle, hypercube)
  return sum(cube.values())


def main():
  global start_h, start_w
  cube = dict()
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

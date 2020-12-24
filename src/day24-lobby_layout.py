from santas_little_helpers import *

today = day(2020, 24)

dirs = {
  'e': (2, 0),
  'se': (1, -1),
  'sw': (-1, -1),
  'w': (-2, 0),
  'nw': (-1, 1),
  'ne': (1, 1)
}


def get_flipped_tiles(inp):
  floor = dict()
  for moves in inp:
    x, y = 0, 0
    for move in moves:
      xd, yd = dirs[move]
      x += xd
      y += yd
    if (x, y) in floor:
      del floor[(x, y)]
    else:
      floor[(x, y)] = True
  return sum(floor.values()), floor


def neighbours(p):
  x, y = p
  for xd, yd in dirs.values():
    yield x + xd, y + yd


def get_adjacent(grid, p):
  x, y = p
  for n_p in neighbours(p):
    if n_p == p or n_p not in grid:
      continue
    yield grid[n_p]


def iterate(grid, points):
  n_grid = dict()
  for p in points:
    active = sum(get_adjacent(grid, p))
    if active == 2:
      n_grid[p] = True
    elif grid.get(p, False) and active == 1:
      n_grid[p] = True
  return n_grid


def game_of_life(grid):
  for cycle in range(100):
    points = set(grid.keys())
    for point in grid.keys():
      points.update(neighbours(point))
    grid = iterate(grid, points)
  return sum(grid.values())


def parse(line):
  idx = 0
  moves = []
  while idx < len(line):
    if line[idx] in 'ew':
      moves.append(line[idx])
      idx += 1
    else:
      moves.append(line[idx:idx + 2])
      idx += 2
  return moves


def main():
  inp = get_data(today, [('func', parse)])
  flipped_tiles, floor = get_flipped_tiles(inp)
  print(f'{today} star 1 = {flipped_tiles}')
  print(f'{today} star 2 = {game_of_life(floor)}')


if __name__ == '__main__':
  timed(main)

from santas_little_helpers import *
from math import sqrt
from copy import deepcopy

today = day(2020, 20)


def get_edges(grid):
  return [
    grid[0],
    [grid[i][-1] for i in range(len(grid))],
    grid[-1],
    [grid[i][0] for i in range(len(grid))]
  ]


def rotate(edges):
  return [
    edges[1],
    list(reversed(edges[2])),
    edges[3],
    list(reversed(edges[0]))
  ]


def flip(edges):
  return [
    list(reversed(edges[0])),
    edges[3],
    list(reversed(edges[2])),
    edges[1],
  ]


def alternatives(grid):
  edges = get_edges(grid)
  e = edges.copy()
  for _ in range(4):
    e = rotate(e)
    yield e
  e = flip(edges.copy())
  for _ in range(4):
    e = rotate(e)
    yield e


def matches(conditions, edges):
  return all(edges[cond] == other for cond, other in conditions.items())


def candidates(consumed=set(), conditions=dict()):
  for tile, grid in grids.items():
    if tile in consumed:
      continue
    for alt in alternatives(grid):
      if matches(conditions, alt):
        yield tile, alt


def fill_empty(image, consumed):
  target = None
  for y in range(height):
    for x in range(width):
      if image[y][x] is None:
        target = (x, y)
        break
    if target is not None:
      break
  if target is None:
    return image
  conditions = {}
  if x > 0:
    conditions[3] = image[y][x - 1]['edges'][1]
  if y > 0:
    conditions[0] = image[y - 1][x]['edges'][2]
  n_image = image.copy()
  n_image[y] = deepcopy(image[y])
  for tile, edges in candidates(consumed, conditions):
    n_image[y][x] = {'tile': tile, 'edges': edges}
    result = fill_empty(n_image, consumed | {tile})
    if result is not None:
      return result
  return None


def part1():
  found = fill_empty([[None for _ in range(width)] for _ in range(height)], set())
  count = found[0][0]['tile']
  count *= found[0][-1]['tile']
  count *= found[-1][0]['tile']
  count *= found[-1][-1]['tile']
  return count


def part2(grids):
  print(grids)


def parse(group):
  lines = group.split('\n')
  tile = int(lines[0][5:-1])
  grid = lines[1:]
  grid = [[grid[y][x] for x in range(len(grid[0]))] for y in range(len(grid))]
  return tile, grid


def main():
  global width, height, grids
  grids = dict(get_data(today, [
    ('func', parse)
  ], groups=True))
  width = height = int(sqrt(len(grids)))
  star1 = part1()
  print(f'{today} star 1 = {star1}')
  # submit_answer(today, star1)
  # star2 = part2(grids)
  # print(f'{today} star 2 = {star2}')
  # submit_answer(today, star2, 2)


if __name__ == '__main__':
  timed(main)

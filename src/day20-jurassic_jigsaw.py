from santas_little_helpers import *
from math import sqrt

today = day(2020, 20)


def rotate(grid): return [list(reversed(row)) for row in zip(*grid)]
def flip(grid): return [list(reversed(row)) for row in grid]


def edges(g):
  rows = list(range(len(g)))
  return [g[0], [g[i][-1] for i in rows], g[-1], [g[i][0] for i in rows]]


def alternatives(grid):
  for _ in range(4):
    grid = rotate(grid)
    yield edges(grid), grid
  grid = flip(grid)
  for _ in range(4):
    grid = rotate(grid)
    yield edges(grid), grid


def matches(conditions, edges):
  return all(edges[cond] == other for cond, other in conditions.items())


def candidates(consumed, conditions):
  for tile, alternatives in grids.items():
    if tile in consumed:
      continue
    for alt, g in alternatives:
      if matches(conditions, alt):
        yield tile, alt, g


def lay_puzzle(puzzle, consumed=set()):
  for x, y in all_coords(width, height):
    if puzzle[y][x] is None:
      break
  else:
    return puzzle
  conditions = {}
  if x > 0:
    conditions[3] = puzzle[y][x - 1]['edges'][1]
  if y > 0:
    conditions[0] = puzzle[y - 1][x]['edges'][2]
  n_puzzle = puzzle.copy()
  n_puzzle[y] = puzzle[y].copy()
  for tile, edges, g in candidates(consumed, conditions):
    n_puzzle[y][x] = {'tile': tile, 'edges': edges, 'grid': g}
    result = lay_puzzle(n_puzzle, consumed | {tile})
    if result is not None:
      return result
  return None


def trim(grid):
  return [row[1:-1] for row in grid[1:-1]]


def reconstruct_image(puzzle_data):
  trimmed = [[trim(item['grid']) for item in row] for row in puzzle_data]
  t_h, t_w = len(trimmed[0][0]), len(trimmed[0][0][0])
  image = [[] for _ in range(height * t_w)]
  for y, grids in enumerate(trimmed):
    for yd, line in [t for grid in grids for t in enumerate(grid)]:
      image[y * t_h + yd].extend(line)
  return image


def solve_puzzle():
  puzzle_data = [[None for _ in range(width)] for _ in range(height)]
  puzzle_data = lay_puzzle(puzzle_data)

  checksum = puzzle_data[0][0]['tile']
  checksum *= puzzle_data[0][-1]['tile']
  checksum *= puzzle_data[-1][0]['tile']
  checksum *= puzzle_data[-1][-1]['tile']

  return checksum, reconstruct_image(puzzle_data)


def find_monsters(image, monster):
  m_h, m_w = len(monster), len(monster[0])
  subgrid_h, subgrid_w = len(image) - m_h, len(image[0]) - m_w
  return sum(all(image[y + m_y][x + m_x] == '#' or not monster[m_y][m_x]
                 for m_x, m_y in all_coords(m_w, m_h))
             for x, y in all_coords(subgrid_w, subgrid_h))


def habitat_rougness(image):
  monster = ['                  # ',
             '#    ##    ##    ###',
             ' #  #  #  #  #  #   ']
  monster = [[c if c != ' ' else None for c in line] for line in monster]
  for _, monster in alternatives(monster):
    result = find_monsters(image, monster)
    if result > 0:
      break
  return str(image).count('#') - str(monster).count('#') * result


def parse(group):
  lines = group.split('\n')
  tile = int(lines[0][5:-1])
  grid = lines[1:]
  grid = [[grid[y][x] for x in range(len(grid[0]))] for y in range(len(grid))]
  return tile, list(alternatives(grid))


def main():
  global width, height, grids
  grids = dict(get_data(today, [('func', parse)], groups=True))
  width = height = int(sqrt(len(grids)))
  checksum, image = solve_puzzle()
  print(f'{today} star 1 = {checksum}')
  print(f'{today} star 2 = {habitat_rougness(image)}')


if __name__ == '__main__':
  timed(main)

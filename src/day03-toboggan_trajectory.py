from santas_little_helpers import day, get_data, timed

today = day(2020, 3)


def predict_slope(xp, yp):
  x = xp
  y = yp
  trees = 0
  while y < slope_length:
    trees += forest[y][x % map_width] == '#'
    x += xp
    y += yp
  return trees


def solve():
  slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
  tree_product = 1
  for i, slope in enumerate(slopes):
    trees = predict_slope(*slope)
    if i == 1:
      yield trees
    tree_product *= trees
  yield tree_product


def main():
  global forest, map_width, slope_length
  forest = list(get_data(today))
  slope_length, map_width = len(forest), len(forest[0])

  star1, star2 = solve()
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {star2}')


if __name__ == '__main__':
  timed(main)

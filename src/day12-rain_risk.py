from santas_little_helpers import *

today = day(2020, 12)

dirs = {
  'N': (0, 1),
  'E': (1, 0),
  'S': (0, -1),
  'W': (-1, 0)
}


def rotate(xd, yd, action, degrees):
  for _ in range(degrees // 90):
    xd, yd = (-yd, xd) if action == 'L' else (yd, -xd)
  return xd, yd


def move(x, y, xd, yd, steps):
  return x + xd * steps, y + yd * steps


def navigate(navigation_input):
  position = 0, 0
  direction = dirs['E']
  for action, value in navigation_input:
    if action in 'LR':
      direction = rotate(*direction, action, value)
    elif action in 'NEWS':
      position = move(*position, *dirs[action], value)
    elif action == 'F':
      position = move(*position, *direction, value)
  return sum(map(abs, position))


def navigate_with_waypoint(navigation_input):
  position = 0, 0
  waypoint = 10, 1
  for action, value in navigation_input:
    if action in 'LR':
      waypoint = rotate(*waypoint, action, value)
    elif action in 'NEWS':
      waypoint = move(*waypoint, *dirs[action], value)
    elif action == 'F':
      position = move(*position, *waypoint, value)
  return sum(map(abs, position))


def parse(line):
  action = line[0]
  value = int(line[1:])
  return action, value


def main():
  navigation_input = list(get_data(today, [('func', parse)]))
  print(f'{today} star 1 = {navigate(navigation_input)}')
  print(f'{today} star 2 = {navigate_with_waypoint(navigation_input)}')


if __name__ == '__main__':
  timed(main)

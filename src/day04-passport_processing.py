from santas_little_helpers import day, get_data, timed
import re

today = day(2020, 4)

req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
hair_colour_re = re.compile(r'^#[0-9a-f]{6}$')


def is_number(data, count):
  try:
    int(data)
    return len(data) == count
  except Exception:
    return False


def is_num_between(data, min_v, max_v):
  try:
    return min_v <= int(data) <= max_v
  except Exception:
    return False


def valid_height(data):
  if 'in' in data:
    return is_num_between(data.replace('in', ''), 59, 76)
  if 'cm' in data:
    return is_num_between(data.replace('cm', ''), 150, 193)
  return False


def valid_hair_colour(data):
  return hair_colour_re.match(data) is not None


def passport_complete(passport):
  return all(field in passport for field in req_fields)


def passport_valid(passport):
  return all([
    is_num_between(passport['byr'], 1920, 2002),
    is_num_between(passport['iyr'], 2010, 2020),
    is_num_between(passport['eyr'], 2020, 2030),
    valid_height(passport['hgt']),
    valid_hair_colour(passport['hcl']),
    passport['ecl'] in eye_colors,
    is_number(passport['pid'], 9)
  ])


def parse(data):
  return dict(segment.split(':') for segment in data.split())


def main():
  passports = list(get_data(today, [('func', parse)], groups=True))
  complete_passports = list(filter(passport_complete, passports))
  print(f'{today} star 1 = {len(complete_passports)}')
  print(f'{today} star 2 = {sum(map(passport_valid, complete_passports))}')


if __name__ == '__main__':
  timed(main)

import json, re, time, importlib, sys, os
from datetime import date
from pathlib import Path
from typing import Callable, Iterator

alphabet = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = alphabet.upper()

base_ops = [('replace', (r'\n', ''))]

aoc_root = Path('../')
aoc_data = aoc_root / 'data'

with (aoc_root / 'config.json').open('r') as f:
  config = json.load(f)


def day(year: int, theday: int) -> date:
  return date(year, 12, theday)


def format_line(line: str, ops: list):
  for op, args in ops:
    if op == 'func':
      line = args(line)
    elif op == 'map':
      line = list(map(args, line))
    elif op == 'replace':
      line = re.sub(args[0], args[1], line)
    elif op == 'split':
      line = line.split(args)
  return line


def get_data(today: date = date.today(), ops: list = base_ops) -> Iterator:
  if not aoc_data.exists():
    aoc_data.mkdir()

  def save_daily_input(today: date) -> None:
    request, status_codes = import_requests()
    url = f'https://adventofcode.com/{today.year}/day/{today.day}/input'
    res = request('GET', url, cookies=config)
    if res.status_code != status_codes.ok:
      print(f'Day {today.day} not available yet')
      sys.exit(0)
    with file_path.open('wb') as f:
      for chunk in res.iter_content(chunk_size=128):
        f.write(chunk)
        print(chunk.decode('utf-8'), end='')
      print()

  file_path = aoc_data / f'day{today.day:02}.txt'
  if not file_path.exists():
    print(f'Data for day {today.day} not available, downloading!')
    save_daily_input(today)
  with file_path.open() as f:
    for line in f.readlines():
      yield format_line(line, ops)


def submit_answer(today: date, answer: str, level: int = 1) -> None:
  from bs4 import BeautifulSoup
  request, status_codes = import_requests()
  url = f'https://adventofcode.com/{today.year}/day/{today.day}/answer'
  payload = {'level': level, 'answer': answer}
  res = request('POST', url, cookies=config, data=payload)
  soup = BeautifulSoup(res.content, 'html.parser')
  for content in soup.find_all('article'):
    print(content.text)


def import_requests():
  from requests import request, codes
  return request, codes


def time_fmt(delta: float) -> (float, str):
  if delta < 1e-6:
    return 1e9, 'ns'
  elif delta < 1e-3:
    return 1e6, 'µs'
  elif delta < 1:
    return 1e3, 'ms'
  return 1, 'seconds'


def execute(func: Callable) -> float:
  start = time.time()
  func()
  return time.time() - start


def execute_multiple(func: Callable, times: int) -> [float]:
  deltas = [execute(func)]
  disable_stdout()
  for _ in range(times - 1):
    deltas += [execute(func)]
  enable_stdout()
  return deltas


def timed(func: Callable) -> None:
  delta = execute(func)
  print_result(delta)


def disable_stdout() -> None:
  sys.stdout = open(os.devnull, 'w')


def enable_stdout() -> None:
  sys.stdout = sys.__stdout__


def bench(func: Callable, times: int = 100):
  deltas = execute_multiple(func, times)
  print_result(min(deltas), 'min')
  avg = sum(deltas) / len(deltas)
  print_result(avg, 'avg')


def average(func: Callable, times: int = 100):
  deltas = execute_multiple(func, times)
  avg = sum(deltas) / len(deltas)
  print_result(avg, 'avg')


def print_result(delta: [float], prefix: str = ''):
  multiplier, unit = time_fmt(delta)
  divider = ''
  if prefix is not '':
    divider = ': '
  print(f'--- {prefix}{divider}{delta*multiplier:.2f} {unit} ---')


def run_all():
  for file in sorted(Path('.').glob('day*-*.py')):
    print(f'Running \'{file.name}\':')
    day = importlib.import_module(file.name[:-3])
    timed(day.main)
    print()


if __name__ == '__main__':
  timed(run_all)

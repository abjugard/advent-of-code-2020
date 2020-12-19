from santas_little_helpers import *
import re

today = day(2020, 19)


def some(res): return f"({'|'.join(res)})"
def every(res): return ''.join(res)
def n(i): return '{' + str(i) + '}'


def build_re(rule_id):
  if rule_id in resolved:
    return resolved[rule_id]

  ors = rules[rule_id]
  and_res = []
  for ands in ors:
    and_res.append(every(build_re(rule_id) for rule_id in ands))

  return some(and_res)


def valid(messages, loops=False):
  if loops:
    r_42 = build_re(42)
    r_31 = build_re(31)
    resolved[8] = f'{r_42}+'
    resolved[11] = some(f'{r_42}{n(i)}{r_31}{n(i)}' for i in range(1, 10))

  r = re.compile(f'^{build_re(0)}$')
  return sum(1 for msg in messages if r.match(msg))


def parse(inp):
  global rules, resolved
  separator = inp.index('')
  rules, resolved = dict(), dict()
  for line in inp[:separator]:
    rule_id, data = line.split(': ')
    rule_id = int(rule_id)
    if data.startswith('"'):
      resolved[rule_id] = data[1]
    else:
      rules[rule_id] = ors = []
      for ors_data in data.split(' | '):
        ors.append(list(map(int, ors_data.split(' '))))
  messages = inp[separator + 1:]
  return messages


def main():
  messages = parse(list(get_data(today)))
  print(f'{today} star 1 = {valid(messages)}')
  print(f'{today} star 2 = {valid(messages, loops=True)}')


if __name__ == '__main__':
  timed(main)

from santas_little_helpers import *
from operator import add, mul

today = day(2020, 18)


def consume(expr):
  op = add
  acc = 0
  for part in expr:
    if part in [add, mul]:
      op = part
    else:
      acc = op(acc, part)
  return acc


def consume_adds(expr):
  while any(p == add for p in expr):
    next_add = expr.index(add)
    value = expr[next_add - 1] + expr[next_add + 1]
    expr = expr[:next_add - 1] + [value] + expr[next_add + 2:]
  return expr


def stupid_math(line):
  return consume(build_expression(line))


def monster_math(line):
  expr = build_expression(line, monster_math)
  expr = consume_adds(expr)
  return consume(expr)


def find_closing(line):
  level = -1
  for idx, c in enumerate(line):
    if c == ')':
      if level == 0:
        return idx + 1
      level -= 1
    if c == '(':
      level += 1


def build_expression(line, fun=stupid_math):
  expr = []
  idx = 0
  while idx < len(line):
    offset = 1
    c = line[idx]
    if c in '123456789':
      expr.append(int(c))
    elif c == '+':
      expr.append(add)
    elif c == '*':
      expr.append(mul)
    elif c == '(':
      offset = find_closing(line[idx:])
      value = fun(line[idx + 1:idx + offset - 1])
      expr.append(value)
    idx += offset
  return expr


def acc(fake_math, fun=stupid_math):
  s = 0
  for line in fake_math:
    s += fun(line)
  return s


def main():
  fake_math = list(get_data(today, base_ops + [('replace', (' ', ''))]))
  print(f'{today} star 1 = {acc(fake_math)}')
  print(f'{today} star 2 = {acc(fake_math, monster_math)}')


if __name__ == '__main__':
  timed(main)

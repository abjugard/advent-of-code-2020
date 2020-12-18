from santas_little_helpers import *
from operator import add, mul

today = day(2020, 18)


def consume(expr):
  op, acc = add, 0
  for part in expr:
    if part in [add, mul]:
      op = part
    else:
      acc = op(acc, part)
  return acc


def left_to_right(eqn):
  expr = build_expression(eqn, left_to_right)
  return consume(expr)


def addition_first(eqn):
  expr = build_expression(eqn, addition_first)
  while any(part == add for part in expr):
    next_add = expr.index(add)
    l, r = next_add - 1, next_add + 1
    expr = expr[:l] + [expr[l] + expr[r]] + expr[r + 1:]
  return consume(expr)


def find_eqn(s):
  level = 0
  for idx, c in enumerate(s):
    if c == ')':
      if level == 1:
        return s[1:idx], idx + 1
      level -= 1
    if c == '(':
      level += 1


def build_expression(line, solve):
  expr = []
  idx = 0
  while idx < len(line):
    skip = 1
    c = line[idx]
    if c in '123456789':
      expr.append(int(c))
    elif c == '+':
      expr.append(add)
    elif c == '*':
      expr.append(mul)
    elif c == '(':
      eqn, skip = find_eqn(line[idx:])
      expr.append(solve(eqn))
    idx += skip
  return expr


def main():
  homework = list(get_data(today, base_ops + [('replace', (' ', ''))]))
  print(f'{today} star 1 = {sum(left_to_right(eqn) for eqn in homework)}')
  print(f'{today} star 2 = {sum(addition_first(eqn) for eqn in homework)}')


if __name__ == '__main__':
  timed(main)

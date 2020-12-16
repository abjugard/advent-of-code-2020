from santas_little_helpers import *

today = day(2020, 16)

ticket_range = None


def validate(rules, all_tickets):
  ticket_scanning_error_rate = 0
  for ticket in all_tickets:
    valid = True
    for value in ticket:
      if all(value not in rule for rule in rules.values()):
        ticket_scanning_error_rate += value
        valid = False
    if valid:
      yield ticket
  yield ticket_scanning_error_rate


def valid_indices(tickets, rule):
  return [i for i in ticket_range if all(t[i] in rule for t in tickets)]


def departure_info(rules, my_ticket, tickets):
  mappings = {f: valid_indices(tickets, rule) for f, rule in rules.items()}
  resolved = 0
  departure_info = 1
  while resolved < len(rules):
    field, idx = next((f, x[0]) for f, x in mappings.items() if len(x) == 1)
    if field.startswith('departure'):
      departure_info *= my_ticket[idx]
    for options in [o for o in mappings.values() if idx in o]:
      options.remove(idx)
    resolved += 1
  return departure_info


def valid_range(data):
  left, right = map(int, data.split('-'))
  return set(range(left, right + 1))


def map_ticket(line):
  return list(map(int, line.split(',')))


def parse(inp):
  global ticket_range
  rules = {}
  for line in inp:
    if line == '':
      break
    field, data = line.split(': ')
    range1, range2 = data.split(' or ')
    rules[field] = valid_range(range1) | valid_range(range2)

  my_ticket = map_ticket(skip(1, inp))
  ticket_range = range(len(my_ticket))

  skip(1, inp)
  all_tickets = [map_ticket(line) for line in inp]
  return rules, my_ticket, all_tickets


def main():
  rules, my_ticket, all_tickets = parse(get_data(today))
  *valid_tickets, ticket_scanning_error_rate = validate(rules, all_tickets)
  print(f'{today} star 1 = {ticket_scanning_error_rate}')
  print(f'{today} star 2 = {departure_info(rules, my_ticket, valid_tickets)}')


if __name__ == '__main__':
  timed(main)

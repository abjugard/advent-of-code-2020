from santas_little_helpers import *
from collections import defaultdict

today = day(2020, 14)


def apply_mask(mask, arg):
  bs = '{0:b}'.format(arg).zfill(36)
  result = [m if m != 'X' else bs[i] for i, m in enumerate(mask)]
  return int(''.join(result), 2)


def execute(bootcode):
  memory = defaultdict(int)
  mask = None
  for instr, arg in bootcode:
    if instr == 'mask':
      mask = arg
    else:
      addr, value = arg
      memory[addr] = apply_mask(mask, value)
  return sum(memory.values())


def insert_bitvalues(baddr, i, xp):
  bs = '{0:b}'.format(i).zfill(len(xp))
  for i, pos in enumerate(xp):
    baddr[pos] = bs[i]
  return int(''.join(baddr), 2)


def apply_memmask(mask, mem):
  baddr = list('{0:b}'.format(mem).zfill(36))
  xp = []
  for i, m in enumerate(mask):
    if m == '1':
      baddr[i] = m
    if m == 'X':
      xp.append(i)
  for i in range(pow(2, len(xp))):
    yield insert_bitvalues(baddr.copy(), i, xp)


def execute_v2(bootcode):
  memory = defaultdict(int)
  mask = None
  for instr, arg in bootcode:
    if instr == 'mask':
      mask = arg
    else:
      addr, value = arg
      addrs = apply_memmask(mask, addr)
      for addr in addrs:
        memory[addr] = value
  return sum(memory.values())


def parse(line):
  instr, arg = line.split(' = ')
  if instr == 'mask':
    return instr, arg
  else:
    addr = int(instr[4:-1])
    value = int(arg)
    return 'mem', (addr, value)


def main():
  bootcode = list(get_data(today, [('func', parse)]))
  print(f'{today} star 1 = {execute(bootcode)}')
  print(f'{today} star 2 = {execute_v2(bootcode)}')


if __name__ == '__main__':
  timed(main)

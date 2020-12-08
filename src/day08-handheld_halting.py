from santas_little_helpers import *
from dataclasses import dataclass

today = day(2020, 8)


@dataclass
class Registers(CpuRegisters):
  acc: int = 0


def nop(regs, _):
  regs.inc_pc()


def jmp(regs, arg):
  regs.inc_pc(arg)


def acc(regs, arg):
  regs.acc += arg
  regs.inc_pc()


def execute(program):
  pcs = set()
  regs = Registers()
  while regs.pc < len(program):
    if regs.pc in pcs:
      return regs.acc, -1
    pcs.add(regs.pc)
    instr, args = program[regs.pc]
    instr(regs, *args)
  return regs.acc, 0


def correct_bug(program):
  for i, (instr, arg) in enumerate(program):
    if instr is acc:
      continue
    derived = program.copy()
    derived[i] = (jmp if instr is nop else nop, arg)
    result, exit_code = execute(derived)
    if exit_code == 0:
      return result


def main():
  program = list(get_data(today, [('asmbunny', [nop, jmp, acc])]))
  print(f'{today} star 1 = {execute(program)[0]}')
  print(f'{today} star 2 = {correct_bug(program)}')


if __name__ == '__main__':
  timed(main)

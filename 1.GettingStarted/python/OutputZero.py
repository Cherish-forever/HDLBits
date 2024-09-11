#!/usr/bin/python3

from migen import *
from migen.fhdl import verilog

class OutputZero(Module):
    def __init__(self):
        self.zero = Signal()
        self.comb += self.zero.eq(0)


if __name__ == "__main__":
    top = OutputZero()
    print(verilog.convert(top, ios={top.zero}))

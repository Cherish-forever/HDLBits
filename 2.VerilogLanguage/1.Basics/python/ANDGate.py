#!/usr/bin/python3

from migen import *
from migen.fhdl import verilog

class ANDGate(Module):
    def __init__(self):
        self.a = Signal()
        self.b = Signal()
        self.out = Signal()

        self.comb += self.out.eq(self.a & self.b)

if __name__ == "__main__":
    top = ANDGate()
    print(verilog.convert(top, ios={top.a, top.b, top.out}))

#!/usr/bin/python3

from migen import *
from migen.fhdl import verilog

class NorGate(Module):
    def __init__(self):
        self.a = Signal()
        self.b = Signal()
        self.out = Signal()
        self.comb += self.out.eq(~(self.a & self.b))

if __name__ == "__main__":
    top = NorGate()
    print(verilog.convert(top, ios={top.out, top.a, top.b}))

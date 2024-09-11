#!/usr/bin/python3

from migen import *
from migen.fhdl import verilog

class DeclaringWires(Module):
    def __init__(self):
        self.a = Signal()
        self.b = Signal()
        self.c = Signal()
        self.d = Signal()
        self.out = Signal()
        self.out_n = Signal()

        self.comb += self.out.eq((self.a & self.b) | (self.c & self.d))
        self.comb += self.out_n.eq(~self.out)

if __name__ == "__main__":
    top = DeclaringWires()
    print(verilog.convert(top, ios={top.a, top.b, top.c,
                                    top.out, top.out_n}))

#!/usr/bin/python3

from migen import *
from migen.fhdl import verilog

class FourWires(Module):
    def __init__(self):
        self.a = Signal()
        self.b = Signal()
        self.c = Signal()
        self.w = Signal()
        self.x = Signal()
        self.y = Signal()
        self.z = Signal()

        self.comb += self.w.eq(self.a)
        self.comb += self.x.eq(self.b)
        self.comb += self.y.eq(self.b)
        self.comb += self.z.eq(self.c)

if __name__ == "__main__":
    top = FourWires()
    print(verilog.convert(top, ios={top.a, top.b, top.c,
                                    top.w, top.x, top.y, top.z}))

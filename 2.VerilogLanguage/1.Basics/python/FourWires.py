#!/usr/bin/python3

from nmigen import *
from nmigen.back import verilog

class FourWires(Elaboratable):
    def __init__(self):
        self.a = Signal()
        self.b = Signal()
        self.c = Signal()
        self.w = Signal()
        self.x = Signal()
        self.y = Signal()
        self.z = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.w.eq(self.a)
        m.d.comb += self.x.eq(self.b)
        m.d.comb += self.y.eq(self.b)
        m.d.comb += self.z.eq(self.c)
        return m

if __name__ == "__main__":
    top = FourWires()
    print(verilog.convert(top, ports=[top.a, top.b, top.c,
                                      top.w, top.x, top.y, top.z]))

#!/usr/bin/python3

from nmigen import *
from nmigen.back import verilog

class DeclaringWires(Elaboratable):
    def __init__(self):
        self.a = Signal()
        self.b = Signal()
        self.c = Signal()
        self.d = Signal()
        self.out = Signal()
        self.out_n = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.out.eq((self.a & self.b) | (self.c & self.d))
        m.d.comb += self.out_n.eq(~self.out)
        return m

if __name__ == "__main__":
    top = DeclaringWires()
    print(verilog.convert(top, ports=[top.a, top.b, top.c,
                                      top.out, top.out_n]))

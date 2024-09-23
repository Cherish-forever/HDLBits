#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class VectorConncatenationOperator(Elaboratable):
    def __init__(self):
        self.a = Signal(5)
        self.b = Signal(5)
        self.c = Signal(5)
        self.d = Signal(5)
        self.e = Signal(5)
        self.f = Signal(5)
        self.w = Signal(8)
        self.x = Signal(8)
        self.y = Signal(8)
        self.z = Signal(8)

    def elaborate(self, platform):
        m = Module()
        # Cat: The first argument occupies the lower bits of the result.
        m.d.comb += self.w.eq(Cat(self.b[2:5], self.a))
        m.d.comb += self.x.eq(Cat(self.d[4], self.c, self.b[0:2]))
        m.d.comb += self.y.eq(Cat(self.e[1:5], self.d[0:4]))
        m.d.comb += self.z.eq(Cat(C(3), self.f, self.e[0]))
        return m

if __name__ == "__main__":
    top = VectorConncatenationOperator()
    main(top, ports=[top.a, top.b, top.c,
                     top.d, top.e, top.f,
                     top.w, top.x, top.y, top.z])

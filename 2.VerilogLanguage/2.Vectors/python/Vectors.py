#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class Vectors(Elaboratable):
    def __init__(self):
        self.vec = Signal(3)
        self.outv = Signal(3)
        self.o2 = Signal()
        self.o1 = Signal()
        self.o0 = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.outv.eq(self.vec)
        m.d.comb += self.o2.eq(self.vec[2])
        m.d.comb += self.o1.eq(self.vec[1])
        m.d.comb += self.o0.eq(self.vec[0])
        return m

if __name__ == "__main__":
    top = Vectors()
    main(top, ports=[top.vec, top.outv,
                     top.o2, top.o1, top.o0])

#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class ANDGate(Elaboratable):
    def __init__(self):
        self.a = Signal()
        self.b = Signal()
        self.out = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.out.eq(self.a & self.b)
        return m

if __name__ == "__main__":
    top = ANDGate()
    main(top, ports=[top.a, top.b, top.out])

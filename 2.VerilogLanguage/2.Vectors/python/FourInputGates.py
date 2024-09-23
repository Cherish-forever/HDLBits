#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class FourInputGates(Elaboratable):
    def __init__(self):
        self.in_ = Signal(4)
        self.out_and = Signal()
        self.out_or = Signal()
        self.out_xor = Signal()

    def elaborate(self, platform):
        m = Module()

        m.d.comb += self.out_and.eq(self.in_.all())
        m.d.comb += self.out_and.eq(self.in_.any())
        m.d.comb += self.out_and.eq(self.in_.xor())

        return m

if __name__ == "__main__":
    top = FourInputGates()
    main(top, ports=[top.in_,top.out_and,
                     top.out_or, top.out_xor])

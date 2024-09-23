#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class MoreReplication(Elaboratable):
    def __init__(self):
        self.a = Signal()
        self.b = Signal()
        self.c = Signal()
        self.d = Signal()
        self.e = Signal()
        self.out = Signal(25)

    def elaborate(self, platform):
        m = Module()

        # Cat: The first argument occupies the lower bits of the result.
        top = Cat([self.e] * 5, [self.d] * 5, [self.c] * 5, [self.b] * 5, [self.a] * 5)
        bottom = Cat([Cat(self.e, self.d, self.c, self.b, self.a)] * 5)
        m.d.comb += self.out.eq(~(top ^ bottom))
        # When multiplying extension bits, it is important to convert bits into a list

        return m

if __name__ == "__main__":
    top = MoreReplication()
    main(top, ports=[top.a, top.b, top.c,
                     top.d, top.e, top.out])

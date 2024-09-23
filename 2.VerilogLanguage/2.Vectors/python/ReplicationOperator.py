#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class ReplicationOperator(Elaboratable):
    def __init__(self):
        self.in_ = Signal(8)
        self.out = Signal(32)

    def elaborate(self, platform):
        m = Module()

        # Cat: The first argument occupies the lower bits of the result.
        m.d.comb += self.out.eq(Cat(self.in_, [self.in_[7]] * 24))
        # # When multiplying extension bits, it is important to convert bits into a list

        return m

if __name__ == "__main__":
    top = ReplicationOperator()
    main(top, ports=[top.in_, top.out])

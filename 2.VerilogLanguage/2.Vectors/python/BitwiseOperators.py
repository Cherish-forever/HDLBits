#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class BitwiseOperators(Elaboratable):
    def __init__(self):
        self.a = Signal(3)
        self.b = Signal(3)
        self.out_or_bitwise = Signal(3)
        self.out_or_logical = Signal()
        self.out_not = Signal(6)

    def elaborate(self, platform):
        m = Module()

        # bitwise OR
        m.d.comb += self.out_or_bitwise.eq(self.a | self.b)

        # logical OR
        # Cat: The first argument occupies the lower bits of the result.
        m.d.comb += self.out_or_logical.eq(Cat(self.a | self.b).any())

        # Slices work like Python slices, not like VHDL or Verilog slices
        # The first bound is the index of the LSB and is inclusive.
        # The second bound is the index of MSB and is exclusive.
        m.d.comb += self.out_not[0:3].eq(~self.a)
        m.d.comb += self.out_not[3:6].eq(~self.b)

        return m

if __name__ == "__main__":
    top = BitwiseOperators()
    main(top, ports=[top.a,top.b,
                     top.out_or_bitwise,
                     top.out_or_logical, top.out_not])

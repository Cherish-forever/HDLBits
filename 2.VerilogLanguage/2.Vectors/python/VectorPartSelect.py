#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class VectorPartSelect(Elaboratable):
    def __init__(self):
        self.in_ = Signal(32)
        self.out = Signal(32)

    def elaborate(self, platform):
        m = Module()

        # Slices work like Python slices, not like VHDL or Verilog slices
        # The first bound is the index of the LSB and is inclusive.
        # The second bound is the index of MSB and is exclusive.
        m.d.comb += self.out[24:32].eq(self.in_[0:8])
        m.d.comb += self.out[16:24].eq(self.in_[8:16])
        m.d.comb += self.out[8:16].eq(self.in_[16:24])
        m.d.comb += self.out[0:8].eq(self.in_[24:32])
        return m

if __name__ == "__main__":
    top = VectorPartSelect()
    main(top, ports=[top.in_, top.out])

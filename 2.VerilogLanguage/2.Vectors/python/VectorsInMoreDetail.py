#!/usr/bin/python3

from nmigen import *
from nmigen.back import verilog

class VectorsInMoreDetail(Elaboratable):
    def __init__(self):
        self.in_ = Signal(16)
        self.out_hi = Signal(8)
        self.out_lo = Signal(8)

    def elaborate(self, platform):
        m = Module()
        # Slices work like Python slices, not like VHDL or Verilog slices
        # The first bound is the index of the LSB and is inclusive.
        # The second bound is the index of MSB and is exclusive.
        m.d.comb += self.out_hi.eq(self.in_[8:16])
        m.d.comb += self.out_lo.eq(self.in_[0:8])
        return m

if __name__ == "__main__":
    top = VectorsInMoreDetail()
    print(verilog.convert(top, ports=[top.in_, top.out_hi, top.out_lo]))

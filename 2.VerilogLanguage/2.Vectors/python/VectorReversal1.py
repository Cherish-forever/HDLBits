#!/usr/bin/python3

from nmigen import *
from nmigen.back import verilog

def cat_reversal_bits(sig, width):
    # Cat: The first argument occupies the lower bits of the result.
    return Cat(sig[width - 1 - i] for i in range(width))

class VectorReversal1(Elaboratable):
    def __init__(self):
        self.in_ = Signal(8)
        self.out = Signal(8)

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.out.eq(cat_reversal_bits(self.in_, 8))
        return m

if __name__ == "__main__":
    top = VectorReversal1()
    print(verilog.convert(top, ports=[top.in_, top.out]))

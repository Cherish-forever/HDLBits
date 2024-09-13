#!/usr/bin/python3

from nmigen import *
from nmigen.back import verilog

class NorGate(Elaboratable):
    def __init__(self):
        self.a = Signal()
        self.b = Signal()
        self.out = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.out.eq(~(self.a & self.b))
        return m

if __name__ == "__main__":
    top = NorGate()
    print(verilog.convert(top, ports=[top.out, top.a, top.b]))

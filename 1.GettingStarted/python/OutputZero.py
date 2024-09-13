#!/usr/bin/python3

from nmigen import *
from nmigen.back import verilog

class OutputZero(Elaboratable):
    def __init__(self):
        self.zero = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.zero.eq(0)
        return m


if __name__ == "__main__":
    top = OutputZero()
    print(verilog.convert(top, ports=[top.zero]))

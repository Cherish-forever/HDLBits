#!/usr/bin/python3

from nmigen import *
from nmigen.back import verilog

class GettingStared(Elaboratable):
    def __init__(self):
        self.one = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.one.eq(1)
        return m

if __name__ == "__main__":
    top = GettingStared()
    print(verilog.convert(top, ports=[top.one]))

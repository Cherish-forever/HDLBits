#!/usr/bin/python3

from migen import *
from migen.fhdl import verilog

class Chip7458(Module):
    def __init__(self):
        self.p1a = Signal()
        self.p1b = Signal()
        self.p1c = Signal()
        self.p1d = Signal()
        self.p1e = Signal()
        self.p1f = Signal()
        self.p1y = Signal()

        self.p2a = Signal()
        self.p2b = Signal()
        self.p2c = Signal()
        self.p2d = Signal()
        self.p2y = Signal()

        self.comb += self.p1y.eq((self.p1a & self.p1b & self.p1c) | (self.p1d & self.p1e & self.p1f))
        self.comb += self.p2y.eq((self.p2a & self.p2b) | (self.p2c & self.p2d))

if __name__ == "__main__":
    top = Chip7458()
    print(verilog.convert(top, ios={top.p1a, top.p1b, top.p1c, top.p1d, top.p1e, top.p1f,
                                    top.p1y,
                                    top.p2a, top.p2b, top.p2c, top.p2d,
                                    top.p2y}))

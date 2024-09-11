#!/usr/bin/python3

from migen import *
from migen.fhdl import verilog

class SimpleWire(Module):
    def __init__(self):
        self.out = Signal()
        self.in_ = Signal()
        self.comb += self.out.eq(self.in_)


if __name__ == "__main__":
    top = SimpleWire()
    print(verilog.convert(top, ios={top.out, top.in_}))

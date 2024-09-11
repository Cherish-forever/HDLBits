#!/usr/bin/python3

from migen import *
from migen.fhdl import verilog

class GettingStared(Module):
    def __init__(self):
        self.one = Signal()
        self.comb += self.one.eq(1)

if __name__ == "__main__":
    top = GettingStared()
    print(verilog.convert(top, ios={top.one}))

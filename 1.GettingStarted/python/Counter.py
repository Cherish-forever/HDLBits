#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class Counter(Elaboratable):
    def __init__(self, width):
        self.v = Signal(width, reset=0)

    def elaborate(self, platform):
        m = Module()
        m.d.sync += self.v.eq(self.v + 1)
        return m

if __name__ == "__main__":
    top = Counter(width=16)
    main(top, ports=[top.v])

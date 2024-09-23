#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class SimpleWire(Elaboratable):
    def __init__(self):
        self.out = Signal()
        self.in_ = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.out.eq(self.in_)
        return m


if __name__ == "__main__":
    top = SimpleWire()
    main(top, ports=[top.out, top.in_])

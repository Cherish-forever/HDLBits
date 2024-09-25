#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.a = Signal()
        self.b = Signal()
        self.out_comb = Signal()
        self.out_sync = Signal()

    def elaborate(self, platform):
        m = Module()

        m.d.comb += self.out_comb.eq(self.a & self.b)
        m.d.sync += self.out_sync.eq(self.a & self.b)

        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.a, top.b,
                     top.out_comb,
                     top.out_sync])

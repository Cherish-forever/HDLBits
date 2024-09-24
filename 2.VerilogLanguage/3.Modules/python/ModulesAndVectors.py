#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class MyDff(Elaboratable):
    def __init__(self, width):
        self.d = Signal(width)
        self.q = Signal(width)

    def elaborate(self, platform):
        m = Module()
        m.d.sync += self.q.eq(self.d)

        return m


class TopModule(Elaboratable):
    def __init__(self):
        self.d = Signal(8)
        self.q = Signal(8)
        self.sel = Signal(2)

    def elaborate(self, platform):
        m = Module()

        a = MyDff(8)
        b = MyDff(8)
        c = MyDff(8)
        m.submodules.mydff_a = a
        m.submodules.mydff_b = b
        m.submodules.mydff_c = c

        m.d.comb += [
            a.d.eq(self.d),
            b.d.eq(a.q),
            c.d.eq(b.q),
        ]

        with m.If(self.sel == 0b00):
            m.d.comb += self.q.eq(self.d)
        with m.If(self.sel == 0b01):
            m.d.comb += self.q.eq(a.q)
        with m.If(self.sel == 0b10):
            m.d.comb += self.q.eq(b.q)
        with m.If(self.sel == 0b11):
            m.d.comb += self.q.eq(c.q)

        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.d, top.q])

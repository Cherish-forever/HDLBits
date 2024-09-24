#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class MyDff(Elaboratable):
    def __init__(self):
        self.d = Signal()
        self.q = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.sync += self.q.eq(self.d)

        return m


class TopModule(Elaboratable):
    def __init__(self):
        self.d = Signal()
        self.q = Signal()

    def elaborate(self, platform):
        m = Module()

        a = MyDff()
        b = MyDff()
        c = MyDff()
        m.submodules.mydff_a = a
        m.submodules.mydff_b = b
        m.submodules.mydff_c = c

        m.d.comb += [
            a.d.eq(self.d),
            b.d.eq(a.q),
            c.d.eq(b.q),
            self.q.eq(c.q)
        ]
        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.d, top.q])

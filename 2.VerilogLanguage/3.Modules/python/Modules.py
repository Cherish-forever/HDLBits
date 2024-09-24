#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class ModA(Elaboratable):
    def __init__(self):
        self.in1 = Signal()
        self.in2 = Signal()
        self.out = Signal()

    def elaborate(self, platform):
        m = Module()
        # eg: out = in1 & in2
        m.d.comb += self.out.eq(self.in1 & self.in2)
        return m


class TopModule(Elaboratable):
    def __init__(self):
        self.a = Signal()
        self.b = Signal()
        self.out = Signal()

    def elaborate(self, platform):
        m = Module()

        mod_a = ModA()
        m.submodules += mod_a

        m.d.comb += [
            mod_a.in1.eq(self.a),
            mod_a.in2.eq(self.b),
            self.out.eq(mod_a.out)
        ]
        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.a, top.b, top.out])

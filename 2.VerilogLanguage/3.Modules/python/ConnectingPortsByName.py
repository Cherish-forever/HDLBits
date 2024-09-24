#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class ModA(Elaboratable):
    def __init__(self):
        self.in1 = Signal()
        self.in2 = Signal()
        self.in3 = Signal()
        self.in4 = Signal()
        self.out1 = Signal()
        self.out2 = Signal()

    def elaborate(self, platform):
        m = Module()

        # eg: out1 = in1 & in2
        #     out2 = in3 | in4
        m.d.comb += [
            self.out1.eq(self.in1 & self.in2),
            self.out2.eq(self.in3 | self.in4)
        ]
        return m


class TopModule(Elaboratable):
    def __init__(self):
        self.a = Signal()
        self.b = Signal()
        self.c = Signal()
        self.d = Signal()
        self.out1 = Signal()
        self.out2 = Signal()

    def elaborate(self, platform):
        m = Module()

        mod_a = ModA()
        m.submodules += mod_a

        m.d.comb += [
            mod_a.in1.eq(self.a),
            mod_a.in2.eq(self.b),
            mod_a.in3.eq(self.c),
            mod_a.in4.eq(self.d),
            self.out1.eq(mod_a.out1),
            self.out2.eq(mod_a.out2)
        ]
        return m

if __name__ == "__main__":
    top = TopModule()
    # strip_internal_attrs=True: Make generate verilog clean, without internal attribute
    main(top, ports=[top.a, top.b, top.c, top.d, top.out1, top.out2])

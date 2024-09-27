#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.sel = Signal()
        self.a   = Signal(8)
        self.b   = Signal(8)
        self.out = Signal(8)

    def elaborate(self, platform):
        m = Module()

        with m.If(self.sel):
            m.d.comb += self.out.eq(self.a)
        with m.Else():
            m.d.comb += self.out.eq(self.b)

        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.sel, top.a, top.b, top.out])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.a.eq(255)
        yield top.b.eq(128)
        yield top.sel.eq(0)
        yield Settle()
        assert (yield top.out) == 128, "Test case 1 failed"

        yield top.sel.eq(1)
        yield Settle()
        assert (yield top.out) == 255, "Test case 2 failed"

    sim.add_process(process)
    sim.run()

#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.a = Signal(100)
        self.b = Signal(100)
        self.sel = Signal()
        self.out = Signal(100)

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.out.eq(Mux(self.sel, self.b, self.a))
        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.a, top.b, top.sel, top.out])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.a.eq(32769)
        yield top.b.eq(65535)
        yield top.sel.eq(0)
        yield Settle()
        assert (yield top.out) == 32769, "Test case 1 failed"

        yield top.sel.eq(1)
        yield Settle()
        assert (yield top.out) == 65535, "Test case 2 failed"

    sim.add_process(process)
    sim.run()

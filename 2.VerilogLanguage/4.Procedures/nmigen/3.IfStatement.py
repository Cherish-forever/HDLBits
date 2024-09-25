#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.a = Signal()
        self.b = Signal()
        self.sel = Signal(2)
        self.out_assign = Signal()
        self.out_if = Signal()

    def elaborate(self, platform):
        m = Module()

        m.d.comb += self.out_assign.eq(Mux(self.sel.all(), self.b, self.a))
        with m.If(self.sel.all()):
            m.d.comb += self.out_if.eq(self.b)
        with m.Else():
            m.d.comb += self.out_if.eq(self.a)

        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.a, top.b, top.sel,
                     top.out_assign, top.out_if])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.a.eq(1)
        yield top.b.eq(0)
        yield top.sel.eq(0)
        yield Settle()
        assert (yield top.out_assign) == (yield top.out_if) == (yield top.a), "Test case 1 failed"

        yield top.a.eq(1)
        yield top.b.eq(0)
        yield top.sel.eq(1)
        yield Settle()
        assert (yield top.out_assign) == (yield top.out_if) == (yield top.a), "Test case 2 failed"

        yield top.a.eq(1)
        yield top.b.eq(0)
        yield top.sel.eq(2)
        yield Settle()
        assert (yield top.out_assign) == (yield top.out_if) == (yield top.a), "Test case 3 failed"

        yield top.a.eq(1)
        yield top.b.eq(0)
        yield top.sel.eq(3)
        yield Settle()
        assert (yield top.out_assign) == (yield top.out_if) == (yield top.b), "Test case 4 failed"

    sim.add_process(process)
    sim.run()

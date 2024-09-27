#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.sel = Signal(2)
        self.a   = Signal(8)
        self.b   = Signal(8)
        self.c   = Signal(8)
        self.d   = Signal(8)
        self.out = Signal(8)

    def elaborate(self, platform):
        m = Module()

        ab = Signal(8)
        cd = Signal(8)

        m.d.comb += [
            ab.eq(Mux(self.sel[0], self.a, self.b)),
            cd.eq(Mux(self.sel[0], self.c, self.d)),
            self.out.eq(Mux(self.sel[1], ab, cd))
        ]

        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.sel, top.a, top.b, top.c, top.d, top.out])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.a.eq(123)
        yield top.b.eq(255)
        yield top.c.eq(10)
        yield top.d.eq(64)
        yield top.sel.eq(0)
        yield Settle()
        assert (yield top.out) == 64, "Test case 1 failed"

        yield top.sel.eq(1)
        yield Settle()
        assert (yield top.out) == 10, "Test case 2 failed"

        yield top.sel.eq(2)
        yield Settle()
        assert (yield top.out) == 255, "Test case 2 failed"

        yield top.sel.eq(3)
        yield Settle()
        assert (yield top.out) == 123, "Test case 3 failed"

    sim.add_process(process)
    sim.run()

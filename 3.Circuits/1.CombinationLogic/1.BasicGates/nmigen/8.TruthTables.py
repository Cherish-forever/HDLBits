#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TruthTables(Elaboratable):
    def __init__(self):
        self.x3 = Signal()
        self.x2 = Signal()
        self.x1 = Signal()
        self.f = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.f.eq((~self.x3 & self.x2 & ~self.x1) |
	                      (~self.x3 & self.x2 & self.x1) |
	                      (self.x3 & ~self.x2 & self.x1) |
	                      (self.x3 & self.x2 & self.x1))
        return m

if __name__ == "__main__":
    top = TruthTables()
    main(top, ports=[top.x3, top.x2, top.x1, top.f])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.x1.eq(0)
        yield top.x2.eq(0)
        yield top.x3.eq(0)
        yield Settle()
        assert (yield top.f) == 0, "Test case 1 failed"

        yield top.x1.eq(1)
        yield top.x2.eq(0)
        yield top.x3.eq(0)
        yield Settle()
        assert (yield top.f) == 0, "Test case 2 failed"

        yield top.x1.eq(0)
        yield top.x2.eq(1)
        yield top.x3.eq(0)
        yield Settle()
        assert (yield top.f) == 1, "Test case 3 failed"

        yield top.x1.eq(1)
        yield top.x2.eq(1)
        yield top.x3.eq(0)
        yield Settle()
        assert (yield top.f) == 1, "Test case 4 failed"

        yield top.x1.eq(0)
        yield top.x2.eq(0)
        yield top.x3.eq(1)
        yield Settle()
        assert (yield top.f) == 0, "Test case 5 failed"

        yield top.x1.eq(1)
        yield top.x2.eq(0)
        yield top.x3.eq(1)
        yield Settle()
        assert (yield top.f) == 1, "Test case 6 failed"

        yield top.x1.eq(0)
        yield top.x2.eq(1)
        yield top.x3.eq(1)
        yield Settle()
        assert (yield top.f) == 0, "Test case 7 failed"

        yield top.x1.eq(1)
        yield top.x2.eq(1)
        yield top.x3.eq(1)
        yield Settle()
        assert (yield top.f) == 1, "Test case 8 failed"

    sim.add_process(process)
    sim.run()

#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class SimpleCircuitB(Elaboratable):
    def __init__(self):
        self.x = Signal()
        self.y = Signal()
        self.z = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.z.eq(~(self.x ^ self.y))
        return m

if __name__ == "__main__":
    top = SimpleCircuitB()
    main(top, ports=[top.x, top.y, top.z])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.x.eq(0)
        yield top.y.eq(0)
        yield Settle()
        assert (yield top.z) == 1, "Test case 1 failed"

        yield top.x.eq(0)
        yield top.y.eq(1)
        yield Settle()
        assert (yield top.z) == 0, "Test case 2 failed"

        yield top.x.eq(1)
        yield top.y.eq(0)
        yield Settle()
        assert (yield top.z) == 0, "Test case 3 failed"

        yield top.x.eq(1)
        yield top.y.eq(1)
        yield Settle()
        assert (yield top.z) == 1, "Test case 4 failed"

    sim.add_process(process)
    sim.run()

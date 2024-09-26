#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class NbitEquality(Elaboratable):
    def __init__(self, width):
        self.a = Signal(width)
        self.b = Signal(width)
        self.z = Signal(width)

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.z.eq(self.a == self.b)
        return m

if __name__ == "__main__":
    top = NbitEquality(2)
    main(top, ports=[top.a, top.b, top.z])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.a.eq(0)
        yield top.b.eq(0)
        yield Settle()
        assert (yield top.z) == 1, "Test case 1 failed"

        yield top.a.eq(0)
        yield top.b.eq(1)
        yield Settle()
        assert (yield top.z) == 0, "Test case 2 failed"

        yield top.a.eq(1)
        yield top.b.eq(0)
        yield Settle()
        assert (yield top.z) == 0, "Test case 3 failed"

        yield top.a.eq(1)
        yield top.b.eq(1)
        yield Settle()
        assert (yield top.z) == 1, "Test case 4 failed"

    sim.add_process(process)
    sim.run()

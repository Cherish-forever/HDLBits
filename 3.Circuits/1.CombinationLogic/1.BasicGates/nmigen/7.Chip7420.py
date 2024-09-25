#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class Chip7420(Elaboratable):
    def __init__(self):
        self.p1y = Signal()
        self.p1a = Signal()
        self.p1b = Signal()
        self.p1c = Signal()
        self.p1d = Signal()
        self.p2y = Signal()
        self.p2a = Signal()
        self.p2b = Signal()
        self.p2c = Signal()
        self.p2d = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += [
            self.p1y.eq(~(self.p1a & self.p1b & self.p1c & self.p1d)),
            self.p2y.eq(~(self.p2a & self.p2b & self.p2c & self.p2d))
        ]
        return m

if __name__ == "__main__":
    top = Chip7420()
    main(top, ports=[top.p1y, top.p1a, top.p1b, top.p1c, top.p1d,
                     top.p2y, top.p2a, top.p2b, top.p2c, top.p2d])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.p1a.eq(0)
        yield top.p1b.eq(0)
        yield top.p1c.eq(0)
        yield top.p1d.eq(0)
        yield top.p2a.eq(1)
        yield top.p2b.eq(1)
        yield top.p2c.eq(1)
        yield top.p2d.eq(1)
        yield Settle()
        assert (yield top.p1y) == 1, "Test case 1.1 failed"
        assert (yield top.p2y) == 0, "Test case 1.2 failed"


        yield top.p1a.eq(1)
        yield top.p1b.eq(1)
        yield top.p1c.eq(1)
        yield top.p1d.eq(1)
        yield top.p2a.eq(0)
        yield top.p2b.eq(0)
        yield top.p2c.eq(0)
        yield top.p2d.eq(0)
        yield Settle()
        assert (yield top.p1y) == 0, "Test case 2.1 failed"
        assert (yield top.p2y) == 1, "Test case 2.2 failed"

        yield top.p1a.eq(1)
        yield top.p1b.eq(0)
        yield top.p1c.eq(1)
        yield top.p1d.eq(0)
        yield top.p2a.eq(1)
        yield top.p2b.eq(0)
        yield top.p2c.eq(1)
        yield top.p2d.eq(0)
        yield Settle()
        assert (yield top.p1y) == 1, "Test case 3.1 failed"
        assert (yield top.p2y) == 1, "Test case 3.2 failed"

        yield top.p1a.eq(1)
        yield top.p1b.eq(1)
        yield top.p1c.eq(1)
        yield top.p1d.eq(1)
        yield top.p2a.eq(1)
        yield top.p2b.eq(1)
        yield top.p2c.eq(1)
        yield top.p2d.eq(1)
        yield Settle()
        assert (yield top.p1y) == 0, "Test case 4.1 failed"
        assert (yield top.p2y) == 0, "Test case 4.2 failed"

    sim.add_process(process)
    sim.run()

#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.x = Signal(4)
        self.f = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += [
            self.f.eq((~self.x[0] & self.x[2]) | (self.x[0] & self.x[1] & ~self.x[2])),
        ]
        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.x, top.f])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.x.eq(0b0000)
        yield Settle()
        assert (yield top.f) == 0, "Test case 1 failed"

        yield top.x.eq(0b0001)
        yield Settle()
        assert (yield top.f) == 0, "Test case 2 failed"

        yield top.x.eq(0b0010)
        yield Settle()
        assert (yield top.f) == 0, "Test case 3 failed"

        yield top.x.eq(0b0011)
        yield Settle()
        assert (yield top.f) == 1, "Test case 4 failed"

        yield top.x.eq(0b0100)
        yield Settle()
        assert (yield top.f) == 1, "Test case 5 failed"

        yield top.x.eq(0b0101)
        yield Settle()
        assert (yield top.f) == 0, "Test case 6 failed"

        yield top.x.eq(0b0110)
        yield Settle()
        assert (yield top.f) == 1, "Test case 7 failed"

        yield top.x.eq(0b0111)
        yield Settle()
        assert (yield top.f) == 0, "Test case 8 failed"

        yield top.x.eq(0b1000)
        yield Settle()
        assert (yield top.f) == 0, "Test case 9 failed"

        yield top.x.eq(0b1001)
        yield Settle()
        assert (yield top.f) == 0, "Test case 10 failed"

        yield top.x.eq(0b1010)
        yield Settle()
        assert (yield top.f) == 0, "Test case 11 failed"

        yield top.x.eq(0b1011)
        yield Settle()
        assert (yield top.f) == 1, "Test case 12 failed"

        yield top.x.eq(0b1100)
        yield Settle()
        assert (yield top.f) == 1, "Test case 13 failed"

        yield top.x.eq(0b1101)
        yield Settle()
        assert (yield top.f) == 0, "Test case 14 failed"

        yield top.x.eq(0b1110)
        yield Settle()
        assert (yield top.f) == 1, "Test case 15 failed"

        yield top.x.eq(0b1111)
        yield Settle()
        assert (yield top.f) == 0, "Test case 16 failed"


    sim.add_process(process)
    sim.run()

#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.a    = Signal(8)
        self.b    = Signal(8)
        self.c    = Signal(8)
        self.d    = Signal(8)
        self.min_ = Signal(8)

    def elaborate(self, platform):
        m = Module()

        ab = Signal(8)
        cd = Signal(8)

        m.d.comb += [
            ab.eq(Mux(self.a < self.b, self.a, self.b)),
            cd.eq(Mux(self.c < self.d, self.c, self.d)),
            self.min_.eq(Mux(ab < cd, ab, cd))
        ]

        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.a, top.b, top.c, top.d, top.min_])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.a.eq(10)
        yield top.b.eq(9)
        yield top.c.eq(8)
        yield top.d.eq(200)
        yield Settle()
        assert (yield top.min_) == 8, "Test case 1 failed"

        yield top.a.eq(64)
        yield top.b.eq(128)
        yield top.c.eq(255)
        yield top.d.eq(32)
        yield Settle()
        assert (yield top.min_) == 32, "Test case 2 failed"


    sim.add_process(process)
    sim.run()

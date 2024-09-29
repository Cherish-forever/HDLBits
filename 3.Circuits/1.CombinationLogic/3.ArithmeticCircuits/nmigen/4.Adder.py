#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.a = Signal(4)
        self.b = Signal(4)
        self.sum_ = Signal(5)

    def elaborate(self, platform):
        m = Module()
        m.d.comb += [
            self.sum_.eq(self.a + self.b)
        ]
        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.a, top.b, top.sum_])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.a.eq(8)
        yield top.b.eq(7)
        yield Settle()
        assert (yield top.sum_) == 15, "Test case 1 failed"

        yield top.a.eq(8)
        yield top.b.eq(8)
        yield Settle()
        assert (yield top.sum_) == 16, "Test case 2 failed"

    sim.add_process(process)
    sim.run()

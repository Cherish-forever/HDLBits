#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.a = Signal()
        self.b = Signal()
        self.cout = Signal()
        self.sum_ = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += [
            self.sum_.eq(self.a ^ self.b),
            self.cout.eq(self.a & self.b)
        ]
        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.a, top.b, top.cout, top.sum_])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.a.eq(0)
        yield top.b.eq(0)
        yield Settle()
        assert (yield top.sum_) == 0, "Test case 1.1 failed"
        assert (yield top.cout) == 0, "Test case 1.2 failed"

        yield top.a.eq(1)
        yield top.b.eq(0)
        yield Settle()
        assert (yield top.sum_) == 1, "Test case 2.1 failed"
        assert (yield top.cout) == 0, "Test case 2.2 failed"

        yield top.a.eq(1)
        yield top.b.eq(1)
        yield Settle()
        assert (yield top.sum_) == 0, "Test case 3.1 failed"
        assert (yield top.cout) == 1, "Test case 3.2 failed"

    sim.add_process(process)
    sim.run()

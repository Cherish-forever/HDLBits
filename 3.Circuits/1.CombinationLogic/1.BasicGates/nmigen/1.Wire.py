#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class Wire(Elaboratable):
    def __init__(self):
        self.in_ = Signal()
        self.out = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.out.eq(self.in_)
        return m

if __name__ == "__main__":
    top = Wire()
    main(top, ports=[top.in_, top.out])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.in_.eq(0)
        yield Settle()
        assert (yield top.out) == 0, "Test case 1 failed"

        yield top.in_.eq(1)
        yield Settle()
        assert (yield top.out) == 1, "Test case 2 failed"

    sim.add_process(process)
    sim.run()

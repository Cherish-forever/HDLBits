#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.in_    = Signal(8)
        self.parity = Signal()

    def elaborate(self, platform):
        m = Module()

        m.d.comb += self.parity.eq(self.in_.xor())

        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.in_, top.parity])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.in_.eq(0b00000001)
        yield Settle()
        assert (yield top.parity) == 1, "Test case 1 failed"

        yield top.in_.eq(0b11111111)
        yield Settle()
        assert (yield top.parity) == 0, "Test case 2 failed"

        yield top.in_.eq(0b11111110)
        yield Settle()
        assert (yield top.parity) == 1, "Test case 3 failed"


    sim.add_process(process)
    sim.run()

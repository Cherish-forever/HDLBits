#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.in_ = Signal(100)
        self.out = Signal(100)

    def elaborate(self, platform):
        m = Module()

        for i in range(100):
            m.d.comb += self.out[i].eq(self.in_[100 - i -1])

        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.in_, top.out])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.in_.eq(0xfffffffff0000000000000000)
        yield Settle()
        assert (yield top.out) == 0xfffffffff, "Test case 1 failed"

    sim.add_process(process)
    sim.run()

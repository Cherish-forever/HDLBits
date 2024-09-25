#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.in_    = Signal(100)
        self.out_and = Signal()
        self.out_or  = Signal()
        self.out_xor = Signal()

    def elaborate(self, platform):
        m = Module()

        m.d.comb += [
            self.out_and.eq(self.in_.all()),
            self.out_or.eq(self.in_.any()),
            self.out_xor.eq(self.in_.xor())
        ]

        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.in_, top.out_and, top.out_or, top.out_xor])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.in_.eq(1)
        yield Settle()
        assert (yield top.out_and) == 0, "Test case 1.1 failed"
        assert (yield top.out_or) == 1, "Test case 1.2 failed"
        assert (yield top.out_xor) == 1, "Test case 1.3 failed"

        yield top.in_.eq(0xfffffffffffffffffffffffff)
        yield Settle()
        assert (yield top.out_and) == 1, "Test case 1.1 failed"
        assert (yield top.out_or) == 1, "Test case 1.2 failed"
        assert (yield top.out_xor) == 0, "Test case 1.3 failed"

    sim.add_process(process)
    sim.run()

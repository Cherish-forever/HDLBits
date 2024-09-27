#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.in_ = Signal(256)
        self.sel = Signal(8)
        self.out = Signal()

    def elaborate(self, platform):
        m = Module()
        for i in range(256):
            with m.If(self.sel == i):
                m.d.comb += self.out.eq(self.in_[i])

        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.in_, top.sel, top.out])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.in_.eq(65535)
        yield top.sel.eq(10)
        yield Settle()
        assert (yield top.out) == 1, "Test case 1 failed"

        yield top.sel.eq(17)
        yield Settle()
        assert (yield top.out) == 0, "Test case 2 failed"

    sim.add_process(process)
    sim.run()

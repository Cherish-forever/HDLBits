#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.in_ = Signal(1024)
        self.sel = Signal(8)
        self.out = Signal(4)

    def elaborate(self, platform):
        m = Module()
        for i in range(256):
            with m.If(self.sel == i):
                m.d.comb += self.out.eq(Cat(self.in_[i * 4 + 3],
                                            self.in_[i * 4 + 2],
                                            self.in_[i * 4 + 1],
                                            self.in_[i * 4]))

        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.in_, top.sel, top.out])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.in_.eq(0xffff)
        yield top.sel.eq(0)
        yield Settle()
        assert (yield top.out) == 0xf, "Test case 1 failed"

        yield top.sel.eq(1)
        yield Settle()
        assert (yield top.out) == 0xf, "Test case 2 failed"

        yield top.sel.eq(2)
        yield Settle()
        assert (yield top.out) == 0xf, "Test case 3 failed"

        yield top.sel.eq(3)
        yield Settle()
        assert (yield top.out) == 0xf, "Test case 4 failed"

        yield top.sel.eq(4)
        yield Settle()
        assert (yield top.out) == 0, "Test case 5 failed"

        yield top.sel.eq(10)
        yield Settle()
        assert (yield top.out) == 0, "Test case 6 failed"

    sim.add_process(process)
    sim.run()

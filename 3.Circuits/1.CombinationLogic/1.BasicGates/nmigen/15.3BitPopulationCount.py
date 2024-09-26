#!/usr/bin/python3

# test no pass, I don`t know why

from nmigen import *
from nmigen.cli import main

# test failed, I don`t know why

class BitsPopulationCount(Elaboratable):
    def __init__(self, width):
        self.in_ = Signal(width)
        self.out = Signal(range(0, width))
        self.width = width

    def elaborate(self, platform):
        m = Module()

        out = Signal(range(0, self.width))
        m.d.comb += out.eq(0)

        for i in range(self.width):
            m.d.comb += out.eq(out + self.in_[i])

        m.d.comb += self.out.eq(out)

        return m

class TopModule(Elaboratable):
    def __init__(self):
        self.in_ = Signal(3)
        self.out = Signal(range(0, 3))

    def elaborate(self, platform):
        m = Module()

        m.submodules.bitscount = bitscount = BitsPopulationCount(3)

        m.d.comb += [
            bitscount.in_.eq(self.in_),
            self.out.eq(bitscount.out)
        ]

        return m


if __name__ == "__main__":
    top = TopModule()
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

        yield top.in_.eq(2)
        yield Settle()
        assert (yield top.out) == 1, "Test case 3 failed"

        yield top.in_.eq(3)
        yield Settle()
        assert (yield top.out) == 2, "Test case 4 failed"

    sim.add_process(process)
    sim.run()

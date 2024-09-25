#!/usr/bin/python3

# test no pass, I don`t know why

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.in_ = Signal(255)
        self.out = Signal(8)

    def elaborate(self, platform):
        m = Module()

        out = Signal(8)
        m.d.comb += out.eq(0)

        for i in range(255):
            m.d.comb += out.eq(out + self.in_[i])

        m.d.comb += self.out.eq(out)

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

        yield top.in_.eq(3)
        yield Settle()
        assert (yield top.out) == 2, "Test case 3 failed"

        yield top.in_.eq(7)
        yield Settle()
        assert (yield top.out) == 3, "Test case 4 failed"

        yield top.in_.eq(0xaaaa)
        yield Settle()
        assert (yield top.out) == 8, "Test case 5 failed"

    sim.add_process(process)
    sim.run()

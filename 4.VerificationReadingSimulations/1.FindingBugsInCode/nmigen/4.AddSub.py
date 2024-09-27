#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.do_sub = Signal()
        self.a   = Signal(8)
        self.b   = Signal(8)
        self.out = Signal(8)
        self.result_is_zero = Signal()

    def elaborate(self, platform):
        m = Module()

        with m.If(self.do_sub):
            m.d.comb += self.out.eq(self.a - self.b)
        with m.Else():
            m.d.comb += self.out.eq(self.a + self.b)

        m.d.comb += self.result_is_zero.eq(self.out == 0)

        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.do_sub, top.a, top.b, top.out, top.result_is_zero])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.a.eq(255)
        yield top.b.eq(100)
        yield top.do_sub.eq(1)
        yield Settle()
        assert (yield top.out) == 155, "Test case 1.1 failed"
        assert (yield top.result_is_zero) == 0, "Test case 1.2 failed"

        yield top.a.eq(100)
        yield top.b.eq(100)
        yield top.do_sub.eq(1)
        yield Settle()
        assert (yield top.out) == 0, "Test case 2.1 failed"
        assert (yield top.result_is_zero) == 1, "Test case 2.2 failed"

        yield top.a.eq(100)
        yield top.b.eq(100)
        yield top.do_sub.eq(0)
        yield Settle()
        assert (yield top.out) == 200, "Test case 3.1 failed"
        assert (yield top.result_is_zero) == 0, "Test case 3.2 failed"

        yield top.a.eq(0)
        yield top.b.eq(0)
        yield top.do_sub.eq(0)
        yield Settle()
        assert (yield top.out) == 0, "Test case 4.1 failed"
        assert (yield top.result_is_zero) == 1, "Test case 4.2 failed"

    sim.add_process(process)
    sim.run()

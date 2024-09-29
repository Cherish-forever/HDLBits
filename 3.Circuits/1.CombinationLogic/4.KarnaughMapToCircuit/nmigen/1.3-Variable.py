#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.a = Signal()
        self.b = Signal()
        self.c = Signal()
        self.out = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += [
            self.out.eq(self.a | self.b | self.c)
        ]
        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.a, top.b, top.c, top.out])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.a.eq(0)
        yield top.b.eq(0)
        yield top.c.eq(0)
        yield Settle()
        assert (yield top.out) == 0, "Test case 1 failed"

        yield top.a.eq(0)
        yield top.b.eq(0)
        yield top.c.eq(1)
        yield Settle()
        assert (yield top.out) == 1, "Test case 2 failed"

        yield top.a.eq(0)
        yield top.b.eq(1)
        yield top.c.eq(0)
        yield Settle()
        assert (yield top.out) == 1, "Test case 3 failed"

        yield top.a.eq(0)
        yield top.b.eq(1)
        yield top.c.eq(1)
        yield Settle()
        assert (yield top.out) == 1, "Test case 4 failed"

        yield top.a.eq(1)
        yield top.b.eq(0)
        yield top.c.eq(0)
        yield Settle()
        assert (yield top.out) == 1, "Test case 5 failed"

        yield top.a.eq(1)
        yield top.b.eq(0)
        yield top.c.eq(1)
        yield Settle()
        assert (yield top.out) == 1, "Test case 6 failed"

        yield top.a.eq(1)
        yield top.b.eq(1)
        yield top.c.eq(0)
        yield Settle()
        assert (yield top.out) == 1, "Test case 7 failed"

        yield top.a.eq(1)
        yield top.b.eq(1)
        yield top.c.eq(1)
        yield Settle()
        assert (yield top.out) == 1, "Test case 8 failed"

    sim.add_process(process)
    sim.run()

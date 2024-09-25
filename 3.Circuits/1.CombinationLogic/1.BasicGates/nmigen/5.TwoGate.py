#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TwoGate(Elaboratable):
    def __init__(self):
        self.in1 = Signal()
        self.in2 = Signal()
        self.in3 = Signal()
        self.out = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.out.eq((~(self.in1 ^ self.in2)) ^ self.in3)
        return m

if __name__ == "__main__":
    top = TwoGate()
    main(top, ports=[top.in1, top.in2, top.out])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield top.in1.eq(0)
        yield top.in2.eq(0)
        yield top.in3.eq(0)
        yield Settle()
        assert (yield top.out) == 1, "Test case 1 failed"

        yield top.in1.eq(0)
        yield top.in2.eq(0)
        yield top.in3.eq(1)
        yield Settle()
        assert (yield top.out) == 0, "Test case 2 failed"

        yield top.in1.eq(0)
        yield top.in2.eq(1)
        yield top.in3.eq(0)
        yield Settle()
        assert (yield top.out) == 0, "Test case 3 failed"

        yield top.in1.eq(0)
        yield top.in2.eq(1)
        yield top.in3.eq(1)
        yield Settle()
        assert (yield top.out) == 1, "Test case 4 failed"

        yield top.in1.eq(1)
        yield top.in2.eq(0)
        yield top.in3.eq(0)
        yield Settle()
        assert (yield top.out) == 0, "Test case 5 failed"

        yield top.in1.eq(1)
        yield top.in2.eq(0)
        yield top.in3.eq(1)
        yield Settle()
        assert (yield top.out) == 1, "Test case 6 failed"

        yield top.in1.eq(1)
        yield top.in2.eq(1)
        yield top.in3.eq(1)
        yield Settle()
        assert (yield top.out) == 0, "Test case 7 failed"

    sim.add_process(process)
    sim.run()

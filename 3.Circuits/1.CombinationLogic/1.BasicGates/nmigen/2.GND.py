#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class GND(Elaboratable):
    def __init__(self):
        self.out = Signal()

    def elaborate(self, platform):
        m = Module()
        m.d.comb += self.out.eq(0)
        return m

if __name__ == "__main__":
    top = GND()
    main(top, ports=[top.out])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
        yield Settle()
        assert (yield top.out) == 0, "Test case 1 failed"

    sim.add_process(process)
    sim.run()

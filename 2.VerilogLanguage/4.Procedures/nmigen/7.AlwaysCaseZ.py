#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.in_ = Signal(8)
        self.pos = Signal(3)

    def elaborate(self, platform):
        m = Module()

        with m.Switch(self.in_):
            with m.Case("-------1"):
                m.d.comb += self.pos.eq(0)
            with m.Case("------10"):
                m.d.comb += self.pos.eq(1)
            with m.Case("-----100"):
                m.d.comb += self.pos.eq(2)
            with m.Case("----1000"):
                m.d.comb += self.pos.eq(3)
            with m.Case("---10000"):
                m.d.comb += self.pos.eq(4)
            with m.Case("--100000"):
                m.d.comb += self.pos.eq(5)
            with m.Case("-1000000"):
                m.d.comb += self.pos.eq(6)
            with m.Case("10000000"):
                m.d.comb += self.pos.eq(7)
            with m.Default():
                m.d.comb += self.pos.eq(0)

        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.pos, top.in_])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
         yield top.in_.eq(0b11111111)
         yield Settle()
         assert (yield top.pos) == 0, "Test case 1 failed"

         yield top.in_.eq(0b11111110)
         yield Settle()
         assert (yield top.pos) == 1, "Test case 2 failed"

         yield top.in_.eq(0b00000100)
         yield Settle()
         assert (yield top.pos) == 2, "Test case 3 failed"

         yield top.in_.eq(0b00001000)
         yield Settle()
         assert (yield top.pos) == 3, "Test case 4 failed"

         yield top.in_.eq(0b11110000)
         yield Settle()
         assert (yield top.pos) == 4, "Test case 5 failed"

         yield top.in_.eq(0b11100000)
         yield Settle()
         assert (yield top.pos) == 5, "Test case 6 failed"

         yield top.in_.eq(0b11000000)
         yield Settle()
         assert (yield top.pos) == 6, "Test case 7 failed"

         yield top.in_.eq(0b10000000)
         yield Settle()
         assert (yield top.pos) == 7, "Test case 8 failed"

    sim.add_process(process)
    sim.run()

#!/usr/bin/python3

from nmigen import *
from nmigen.cli import main

class TopModule(Elaboratable):
    def __init__(self):
        self.in_ = Signal(4)
        self.pos = Signal(2)

    def elaborate(self, platform):
        m = Module()

        with m.Switch(self.in_):
            with m.Case(0):
                m.d.comb += self.pos.eq(0)
            with m.Case(1):
                m.d.comb += self.pos.eq(0)
            with m.Case(2):
                m.d.comb += self.pos.eq(1)
            with m.Case(3):
                m.d.comb += self.pos.eq(0)
            with m.Case(4):
                m.d.comb += self.pos.eq(2)
            with m.Case(5):
                m.d.comb += self.pos.eq(0)
            with m.Case(6):
                m.d.comb += self.pos.eq(1)
            with m.Case(7):
                m.d.comb += self.pos.eq(0)
            with m.Case(8):
                m.d.comb += self.pos.eq(3)
            with m.Case(9):
                m.d.comb += self.pos.eq(0)
            with m.Case(10):
                m.d.comb += self.pos.eq(1)
            with m.Case(11):
                m.d.comb += self.pos.eq(0)
            with m.Case(12):
                m.d.comb += self.pos.eq(2)
            with m.Case(13):
                m.d.comb += self.pos.eq(0)
            with m.Case(14):
                m.d.comb += self.pos.eq(1)
            with m.Case(15):
                m.d.comb += self.pos.eq(0)
            with m.Default():
                m.d.comb += self.pos.eq(0)

        return m

if __name__ == "__main__":
    top = TopModule()
    main(top, ports=[top.pos, top.in_])

    from nmigen.back.pysim import Simulator, Delay, Settle

    sim = Simulator(top)

    def process():
         yield top.in_.eq(0)
         yield Settle()
         assert (yield top.pos) == 0, "Test case 1 failed"

         yield top.in_.eq(1)
         yield Settle()
         assert (yield top.pos) == 0, "Test case 2 failed"

         yield top.in_.eq(2)
         yield Settle()
         assert (yield top.pos) == 1, "Test case 3 failed"

         yield top.in_.eq(3)
         yield Settle()
         assert (yield top.pos) == 0, "Test case 4 failed"

         yield top.in_.eq(4)
         yield Settle()
         assert (yield top.pos) == 2, "Test case 5 failed"

         yield top.in_.eq(5)
         yield Settle()
         assert (yield top.pos) == 0, "Test case 6 failed"

         yield top.in_.eq(6)
         yield Settle()
         assert (yield top.pos) == 1, "Test case 7 failed"

         yield top.in_.eq(7)
         yield Settle()
         assert (yield top.pos) == 0, "Test case 8 failed"

         yield top.in_.eq(8)
         yield Settle()
         assert (yield top.pos) == 3, "Test case 9 failed"

         yield top.in_.eq(9)
         yield Settle()
         assert (yield top.pos) == 0, "Test case 10 failed"

         yield top.in_.eq(10)
         yield Settle()
         assert (yield top.pos) == 1, "Test case 11 failed"

         yield top.in_.eq(11)
         yield Settle()
         assert (yield top.pos) == 0, "Test case 12 failed"

         yield top.in_.eq(12)
         yield Settle()
         assert (yield top.pos) == 2, "Test case 13 failed"

         yield top.in_.eq(13)
         yield Settle()
         assert (yield top.pos) == 0, "Test case 14 failed"

         yield top.in_.eq(14)
         yield Settle()
         assert (yield top.pos) == 1, "Test case 15 failed"

         yield top.in_.eq(15)
         yield Settle()
         assert (yield top.pos) == 0, "Test case 16 failed"

    sim.add_process(process)
    sim.run()
